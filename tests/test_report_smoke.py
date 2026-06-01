"""Smoke test for the one-command status report (src/report.py, was 0% covered).

The report is the project's `python -m src.report` entry point. This test runs it
end-to-end and exercises the individual section printers, so a crash in any
status section (e.g. a renamed registry function) is caught by CI.
"""

from src import report


def test_report_main_runs_end_to_end(capsys):
    report.main()
    out = capsys.readouterr().out
    assert len(out) > 0, "report produced no output"
    # The report should reference the project it summarizes.
    assert any(token in out for token in ("Buckholtz", "IDM", "MULTING"))


def test_each_section_printer_runs(capsys):
    section_fns = [
        "print_header",
        "print_eq15_status",
        "print_beta_status",
        "print_equations_status",
        "print_footer",
    ]
    for name in section_fns:
        getattr(report, name)()
    out = capsys.readouterr().out
    assert len(out) > 0
