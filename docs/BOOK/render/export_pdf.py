"""Phase E addendum -- print book.html to a paginated PDF via headless Chromium.

Run assemble_book.py first (book.html must exist next to this script). Output
is book.pdf, gitignored by this repo's own *.pdf policy -- regenerate locally
rather than expecting it in version control.

Requires: pip install playwright && playwright install chromium

Run: python docs/BOOK/render/export_pdf.py
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

RENDER_DIR = Path(__file__).resolve().parent
SRC = RENDER_DIR / "book.html"
OUT = RENDER_DIR / "book.pdf"


def main() -> None:
    if not SRC.exists():
        raise SystemExit(f"{SRC} not found -- run assemble_book.py first")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(SRC.resolve().as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(OUT),
            format="A4",
            margin={"top": "20mm", "bottom": "20mm", "left": "16mm", "right": "16mm"},
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                '<div style="font-size:8px; width:100%; text-align:center; '
                'color:#888; font-family: monospace;">'
                '<span class="pageNumber"></span> / <span class="totalPages"></span></div>'
            ),
        )
        browser.close()
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
