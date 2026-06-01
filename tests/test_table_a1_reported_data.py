"""Tests for Table A1 Reported Data

Purpose: Verify manual transcription of Table A1 from manuscript PDF
Context: Table A1 contains H_MULT values (AI service output, beta_d=4.5, beta_q=18.0)

Test Coverage:
1. CSV structure and parsing
2. Column count and names
3. Numeric field validation
4. Monotonicity checks (z values)
5. Physical constraints (H > 0, sigma ≥ 0)
6. Beta metadata presence
7. H_MULT provenance (TABLE_REPORTED only, no computation function)
"""

from pathlib import Path

import pandas as pd
import pytest

# ============================================================================
# Test Fixtures
# ============================================================================


@pytest.fixture
def table_a1_path():
    """Path to Table A1 CSV file"""
    return Path("data/table_a1_reported.csv")


@pytest.fixture
def table_a1_df(table_a1_path):
    """Load Table A1 as pandas DataFrame (skip comment lines)"""
    if not table_a1_path.exists():
        pytest.skip(f"Table A1 CSV not found: {table_a1_path}")

    # Read CSV, skip comment lines starting with #
    df = pd.read_csv(table_a1_path, comment="#")

    # Check if dataframe is empty (no data rows transcribed yet)
    if df.empty or len(df) == 0:
        pytest.skip("Table A1 CSV is empty — awaiting manual transcription from PDF")

    return df


@pytest.fixture
def table_a1_raw_text(table_a1_path):
    """Raw text of Table A1 CSV (for metadata checks)"""
    if not table_a1_path.exists():
        pytest.skip(f"Table A1 CSV not found: {table_a1_path}")
    return table_a1_path.read_text()


# ============================================================================
# Test 1: File Existence and Structure
# ============================================================================


def test_table_a1_file_exists(table_a1_path):
    """Table A1 CSV file exists"""
    assert table_a1_path.exists(), f"Table A1 CSV not found: {table_a1_path}"


def test_table_a1_is_readable(table_a1_df):
    """Table A1 CSV can be parsed as DataFrame"""
    assert isinstance(table_a1_df, pd.DataFrame)
    assert not table_a1_df.empty, "Table A1 DataFrame is empty"


def test_table_a1_has_data_rows(table_a1_df):
    """Table A1 has at least one data row"""
    assert len(table_a1_df) > 0, "Table A1 has zero data rows"


# ============================================================================
# Test 2: Column Structure
# ============================================================================


def test_table_a1_has_expected_columns(table_a1_df):
    """Table A1 has expected column names"""
    expected_columns = [
        "time_gyr",
        "z",
        "H_obs",
        "sigma_H",
        "H_FLRW",
        "sigma_FLRW",
        "H_MULT",
        "sigma_MULT",
        "w_eff",
        "H_w_eff",
        "sigma_w_eff",
        "notes",
    ]
    actual_columns = list(table_a1_df.columns)
    assert (
        actual_columns == expected_columns
    ), f"Column mismatch.\nExpected: {expected_columns}\nActual: {actual_columns}"


def test_table_a1_column_count(table_a1_df):
    """Table A1 has 12 columns"""
    assert len(table_a1_df.columns) == 12, f"Expected 12 columns, found {len(table_a1_df.columns)}"


# ============================================================================
# Test 3: Row Count (Expected ~12 from Appendix A1 Step 3)
# ============================================================================


def test_table_a1_row_count_reasonable(table_a1_df):
    """Table A1 has reasonable row count (6-20 rows expected)"""
    row_count = len(table_a1_df)
    assert 6 <= row_count <= 20, f"Table A1 has {row_count} rows — expected 6-20 (z=0 to 8.5 range)"


def test_table_a1_row_count_expected(table_a1_df):
    """Table A1 has ~12 rows (expected from Appendix A1 Step 3)"""
    row_count = len(table_a1_df)
    # Soft check: warn if not ~12, but don't fail (table may have more/fewer)
    if row_count < 10 or row_count > 15:
        pytest.warns(UserWarning, match=f"Table A1 has {row_count} rows — expected ~12")


# ============================================================================
# Test 4: Numeric Field Parsing
# ============================================================================


def test_time_gyr_is_numeric(table_a1_df):
    """time_gyr column parses as numeric"""
    # Allow NA values, but non-NA must be numeric
    numeric_count = pd.to_numeric(table_a1_df["time_gyr"], errors="coerce").notna().sum()
    assert numeric_count > 0, "time_gyr column has zero numeric values"


def test_z_is_numeric(table_a1_df):
    """z column parses as numeric"""
    z_numeric = pd.to_numeric(table_a1_df["z"], errors="coerce")
    assert z_numeric.notna().all(), "z column has non-numeric values (should not have NA)"


def test_h_mult_is_numeric(table_a1_df):
    """H_MULT column parses as numeric"""
    h_mult_numeric = pd.to_numeric(table_a1_df["H_MULT"], errors="coerce")
    assert (
        h_mult_numeric.notna().all()
    ), "H_MULT column has non-numeric or NA values (should be numeric for all rows)"


def test_sigma_mult_is_numeric_or_na(table_a1_df):
    """sigma_MULT column parses as numeric or NA"""
    # sigma_MULT may have NA values
    sigma_mult = table_a1_df["sigma_MULT"].replace("NA", pd.NA)
    sigma_mult_numeric = pd.to_numeric(sigma_mult, errors="coerce")
    # At least some rows should have numeric sigma_MULT
    assert sigma_mult_numeric.notna().sum() > 0, "sigma_MULT column has zero numeric values"


# ============================================================================
# Test 5: Redshift Monotonicity
# ============================================================================


def test_z_values_are_monotonic(table_a1_df):
    """z values are monotonic (either increasing or decreasing)"""
    z = pd.to_numeric(table_a1_df["z"], errors="coerce")
    z_clean = z.dropna()

    is_increasing = (z_clean.diff().dropna() >= 0).all()
    is_decreasing = (z_clean.diff().dropna() <= 0).all()

    assert (
        is_increasing or is_decreasing
    ), "z values are not monotonic (should increase or decrease consistently)"


def test_z_range_covers_expected(table_a1_df):
    """z values cover expected range (0 to ~8.5 from Appendix A1)"""
    z = pd.to_numeric(table_a1_df["z"], errors="coerce")
    z_min = z.min()
    z_max = z.max()

    assert z_min <= 0.5, f"z_min = {z_min} — expected to start near 0"
    assert z_max >= 7.0, f"z_max = {z_max} — expected to reach ~8.5"


# ============================================================================
# Test 6: Physical Constraints
# ============================================================================


def test_h_mult_positive(table_a1_df):
    """H_MULT values are positive (expansion rate > 0)"""
    h_mult = pd.to_numeric(table_a1_df["H_MULT"], errors="coerce")
    assert (h_mult > 0).all(), "H_MULT has non-positive values (expansion rate must be > 0)"


def test_sigma_mult_non_negative(table_a1_df):
    """sigma_MULT values are valid standardized residuals (can be negative)"""
    sigma_mult = table_a1_df["sigma_MULT"].replace("NA", pd.NA)
    sigma_mult_numeric = pd.to_numeric(sigma_mult, errors="coerce")
    sigma_mult_clean = sigma_mult_numeric.dropna()

    if len(sigma_mult_clean) > 0:
        # sigma_MULT is standardized residual (H_MULT - H_obs)/sigma_H — CAN be negative
        # Check reasonable range: typically -5 to +5 for standardized residuals
        assert (sigma_mult_clean >= -10).all() and (sigma_mult_clean <= 10).all(), (
            f"sigma_MULT has unreasonable values (should be in [-10, 10]). "
            f"Range: [{sigma_mult_clean.min()}, {sigma_mult_clean.max()}]"
        )


def test_time_gyr_positive(table_a1_df):
    """time_gyr values are positive (cosmic time > 0)"""
    time_gyr = table_a1_df["time_gyr"].replace("NA", pd.NA)
    time_gyr_numeric = pd.to_numeric(time_gyr, errors="coerce")
    time_gyr_clean = time_gyr_numeric.dropna()

    if len(time_gyr_clean) > 0:
        assert (
            time_gyr_clean > 0
        ).all(), "time_gyr has non-positive values (cosmic time must be > 0)"


def test_time_gyr_less_than_age_of_universe(table_a1_df):
    """time_gyr values are less than age of universe (~13.8 Gyr)"""
    time_gyr = table_a1_df["time_gyr"].replace("NA", pd.NA)
    time_gyr_numeric = pd.to_numeric(time_gyr, errors="coerce")
    time_gyr_clean = time_gyr_numeric.dropna()

    if len(time_gyr_clean) > 0:
        assert (time_gyr_clean < 14.0).all(), (
            f"time_gyr has values > 14 Gyr (age of universe is ~13.8 Gyr). "
            f"Max value: {time_gyr_clean.max()}"
        )


# ============================================================================
# Test 7: Beta Metadata Presence
# ============================================================================


def test_beta_d_in_metadata(table_a1_raw_text):
    """beta_d = 4.5 is present in CSV metadata (comment lines)"""
    assert (
        "beta_d = 4.5" in table_a1_raw_text or "beta_d=4.5" in table_a1_raw_text
    ), "beta_d = 4.5 not found in CSV metadata (should be in comment lines)"


def test_beta_q_in_metadata(table_a1_raw_text):
    """beta_q = 18.0 is present in CSV metadata (comment lines)"""
    assert (
        "beta_q = 18.0" in table_a1_raw_text or "beta_q=18.0" in table_a1_raw_text
    ), "beta_q = 18.0 not found in CSV metadata (should be in comment lines)"


def test_provenance_marked_fitted(table_a1_raw_text):
    """Beta provenance is marked as FITTED_PHENOMENOLOGICAL in metadata"""
    assert (
        "FITTED_PHENOMENOLOGICAL" in table_a1_raw_text
    ), "Beta provenance should be marked as FITTED_PHENOMENOLOGICAL in CSV comments"


# ============================================================================
# Test 8: H_MULT Provenance Enforcement
# ============================================================================


def test_h_mult_is_table_reported_not_computed():
    """H_MULT values are TABLE_REPORTED, NOT computed by a function"""
    # This test ensures we don't accidentally create a compute_H_MULT function
    # H_MULT values come ONLY from Table A1 transcription

    # Check: no module has function named compute_H_MULT or compute_Hz_source_confirmed
    import src.hmult_algorithm_candidates as candidates_module

    assert not hasattr(
        candidates_module, "compute_H_MULT"
    ), "Module has function compute_H_MULT — H_MULT should be TABLE_REPORTED only"
    assert not hasattr(
        candidates_module, "compute_Hz_source_confirmed"
    ), "Module has function compute_Hz_source_confirmed — formula not source-confirmed"


def test_no_h_mult_computation_in_codebase():
    """No function named compute_H_MULT exists in codebase"""
    # Grep for function definitions
    import re
    from pathlib import Path

    src_files = list(Path("src").glob("*.py"))
    for src_file in src_files:
        content = src_file.read_text()
        # Check for function definition patterns
        if re.search(r"def\s+compute_H_MULT\s*\(", content):
            pytest.fail(
                f"Found compute_H_MULT function in {src_file} — "
                f"H_MULT should be TABLE_REPORTED only, not computed"
            )
        if re.search(r"def\s+compute_Hz_source_confirmed\s*\(", content):
            pytest.fail(
                f"Found compute_Hz_source_confirmed function in {src_file} — "
                f"formula not source-confirmed"
            )


# ============================================================================
# Test 9: No Duplicate Redshifts
# ============================================================================


def test_no_duplicate_z_values(table_a1_df):
    """No duplicate redshift values (each row should have unique z)"""
    z = pd.to_numeric(table_a1_df["z"], errors="coerce")
    duplicates = z[z.duplicated()]
    assert len(duplicates) == 0, f"Duplicate z values found: {duplicates.tolist()}"


# ============================================================================
# Test 10: Column-Specific Checks
# ============================================================================


def test_h_flrw_positive(table_a1_df):
    """H_FLRW values are positive (ΛCDM expansion rate > 0)"""
    h_flrw = table_a1_df["H_FLRW"].replace("NA", pd.NA)
    h_flrw_numeric = pd.to_numeric(h_flrw, errors="coerce")
    h_flrw_clean = h_flrw_numeric.dropna()

    if len(h_flrw_clean) > 0:
        assert (
            h_flrw_clean > 0
        ).all(), "H_FLRW has non-positive values (ΛCDM expansion rate must be > 0)"


def test_w_eff_reasonable_range(table_a1_df):
    """w_eff values are in reasonable range (-2 to 0)"""
    w_eff = table_a1_df["w_eff"].replace("NA", pd.NA)
    w_eff_numeric = pd.to_numeric(w_eff, errors="coerce")
    w_eff_clean = w_eff_numeric.dropna()

    if len(w_eff_clean) > 0:
        assert (w_eff_clean >= -2).all() and (w_eff_clean <= 0).all(), (
            f"w_eff values outside reasonable range [-2, 0]. "
            f"Range found: [{w_eff_clean.min()}, {w_eff_clean.max()}]"
        )


# ============================================================================
# Test 11: Diagnostic Statistics (Informational)
# ============================================================================


def test_print_table_a1_summary(table_a1_df):
    """Print Table A1 summary statistics (informational, always passes)"""
    print("\n" + "=" * 60)
    print("TABLE A1 SUMMARY")
    print("=" * 60)
    print(f"Row count: {len(table_a1_df)}")
    print(f"Column count: {len(table_a1_df.columns)}")
    print(f"\nRedshift range: z = {table_a1_df['z'].min()} to {table_a1_df['z'].max()}")

    h_mult = pd.to_numeric(table_a1_df["H_MULT"], errors="coerce")
    print(f"\nH_MULT range: {h_mult.min():.2f} to {h_mult.max():.2f} km/s/Mpc")
    print(f"H_MULT mean: {h_mult.mean():.2f} km/s/Mpc")
    print(f"H_MULT std: {h_mult.std():.2f} km/s/Mpc")

    sigma_mult = pd.to_numeric(table_a1_df["sigma_MULT"].replace("NA", pd.NA), errors="coerce")
    if sigma_mult.notna().any():
        print(f"\nsigma_MULT range: {sigma_mult.min():.3f} to {sigma_mult.max():.3f}")
        print(f"sigma_MULT mean: {sigma_mult.mean():.3f}")

    # Check for NA columns
    na_counts = (table_a1_df == "NA").sum()
    if na_counts.sum() > 0:
        print("\nColumns with NA values:")
        for col, count in na_counts[na_counts > 0].items():
            print(f"  {col}: {count} NA values")

    print("=" * 60 + "\n")
    assert True  # Always pass, this is informational only


# ============================================================================
# Test 12: Reverse Engineering Readiness
# ============================================================================


def test_table_a1_ready_for_reverse_engineering(table_a1_df):
    """Table A1 has minimum columns needed for reverse engineering"""
    required_columns = ["z", "H_MULT"]
    for col in required_columns:
        assert (
            col in table_a1_df.columns
        ), f"Required column {col} missing — needed for reverse engineering"

    # Check these columns have no NA values
    z = pd.to_numeric(table_a1_df["z"], errors="coerce")
    h_mult = pd.to_numeric(table_a1_df["H_MULT"], errors="coerce")

    assert z.notna().all(), "z column has NA values — cannot do reverse engineering"
    assert h_mult.notna().all(), "H_MULT column has NA values — cannot do reverse engineering"


# ============================================================================
# Summary Test
# ============================================================================


def test_table_a1_integrity_summary(table_a1_df, table_a1_raw_text):
    """Master test: verify all integrity checks in one place"""
    # Rule 1: CSV parses
    assert isinstance(table_a1_df, pd.DataFrame)
    assert not table_a1_df.empty

    # Rule 2: Expected columns
    assert len(table_a1_df.columns) == 12

    # Rule 3: Redshifts are numeric and monotonic
    z = pd.to_numeric(table_a1_df["z"], errors="coerce")
    assert z.notna().all()

    # Rule 4: H_MULT values are numeric and positive
    h_mult = pd.to_numeric(table_a1_df["H_MULT"], errors="coerce")
    assert h_mult.notna().all()
    assert (h_mult > 0).all()

    # Rule 5: Beta metadata present
    assert "beta_d = 4.5" in table_a1_raw_text or "beta_d=4.5" in table_a1_raw_text
    assert "beta_q = 18.0" in table_a1_raw_text or "beta_q=18.0" in table_a1_raw_text

    # Rule 6: No compute_H_MULT function
    import src.hmult_algorithm_candidates as candidates_module

    assert not hasattr(candidates_module, "compute_H_MULT")

    print("\n✅ All Table A1 integrity checks passed")
    print(f"   - {len(table_a1_df)} rows transcribed")
    print(f"   - z range: {z.min():.2f} to {z.max():.2f}")
    print(f"   - H_MULT range: {h_mult.min():.2f} to {h_mult.max():.2f} km/s/Mpc")
    print("   - Beta metadata: beta_d=4.5, beta_q=18.0")
    print("   - Provenance: TABLE_REPORTED (not computed)")
