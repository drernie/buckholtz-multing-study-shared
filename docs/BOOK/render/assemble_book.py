"""Phase E — assemble the 22 chapters + 10 figures into one reading-copy HTML.

Reads every chapter Markdown file and the chronology appendix directly from
../chapters/ and ../01_CHRONOLOGY.md, embeds the 10 figure PNGs from
../figures/ as base64 data URIs (no external assets, no network fetch), and
writes book.html next to this script. Re-run after any chapter edit to
regenerate the reading copy; nothing here is hand-copied prose.

Run: python docs/BOOK/render/assemble_book.py
"""

import base64
import html
import re
from pathlib import Path

import markdown

RENDER_DIR = Path(__file__).resolve().parent
ROOT = RENDER_DIR.parent
CH = ROOT / "chapters"
FIG = ROOT / "figures"
OUT = RENDER_DIR / "book.html"

MD = markdown.Markdown(extensions=["extra", "sane_lists", "smarty"])

PARTS = [
    (
        "0",
        "Как читать эту книгу",
        "27 мая — 11 августа 2026",
        [
            ("0.1-boundaries.md", None),
            ("0.2-evidence-apparatus.md", None),
            ("0.3-repo-map.md", "f1_commit_timeline"),
        ],
    ),
    (
        "I",
        "Происхождение",
        "27 мая — 1 июня 2026",
        [
            ("1.1-origins.md", None),
            ("1.2-first-mvp.md", None),
            ("1.3-arithmetic-results.md", "f3_look_elsewhere"),
        ],
    ),
    (
        "II",
        "Охота за мостом",
        "июнь 2026",
        [
            ("2.1-the-bridge-problem.md", None),
            ("2.2-ill-posed-inverse-problem.md", "f2_epsilon_nonmonotone"),
            ("2.3-cemetery-one.md", None),
            ("2.4-correspondence.md", None),
        ],
    ),
    (
        "III",
        "Кластерный цикл и провенанс β",
        "июль 2026",
        [
            ("3.1-h1-cycle.md", None),
            ("3.2-dissolution.md", "f5_h1_correlation_dissolves"),
            ("3.3-beta-not-identifiable.md", "f4_beta_ai_spread"),
            ("3.4-pdg-correction.md", None),
        ],
    ),
    (
        "IV",
        "Кризис провенанса и прямой тест",
        "август 2026",
        [
            ("4.1-table-a1-provenance.md", None),
            ("4.2-four-gates.md", None),
            ("4.3-ksz-direct-test.md", ["f6_ksz_kernels", "f7_ksz_dipole_limit"]),
            ("4.4-two-charge-completion.md", "f8_scaling_exponent"),
        ],
    ),
    (
        "V",
        "Реестр и итог",
        "август 2026",
        [
            ("5.1-ncg-excursion.md", "f10_ncg_nullspace_collapse"),
            ("5.2-catalog-of-errors.md", None),
            ("5.3-full-registry.md", "f9_null_results_timeline"),
            ("5.4-what-i-would-do-differently.md", None),
        ],
    ),
]

FIG_CAPTIONS = {
    "f1_commit_timeline": "F1 — карта работы: коммиты по неделям, с вехами",
    "f2_epsilon_nonmonotone": "F2 — ε(z) немонотонна: пик при z=0.40, ε=0.228",
    "f3_look_elsewhere": "F3 — look-elsewhere: Eq.32 — ранг #1 из 83 160 выражений",
    "f4_beta_ai_spread": "F4 — разброс β по трём ИИ-сервисам: Birge ratio 15.9 / 24.1",
    "f5_h1_correlation_dissolves": "F5 — H1: −0.701 → −0.726 (пережила) → −0.079 (растворилась)",
    "f6_ksz_kernels": "F6 — ядра kSZ C₃(ρ), C₄(ρ): расходимости при ρ→1",
    "f7_ksz_dipole_limit": "F7 — профиль χ²(ℓ_d): нет детекции диполя, p=0.49",
    "f8_scaling_exponent": "F8 — показатель масштабирования: +1 (теория) vs 0.555 (маргинальный) vs 0.393 (деконфаундированный)",
    "f9_null_results_timeline": "F9 — таймлайн 17 нулевых результатов по двум веткам",
    "f10_ncg_nullspace_collapse": "F10 — НКГ: схлопывание нуль-пространства 576→8→1→0→0",
}

TAG_RE = re.compile(
    r"\[(VERIFIED(?:-[A-Z0-9]+)?|HYPOTHESIS|SPECULATIVE|WEAK|INFERRED|CONFLICTING|UNKNOWN|"
    r"CONFIRMED-REAL|FALSIFIED(?:-[A-Za-z-]+)?|WEAKENED|NEEDS-REAL-DATA|"
    r"Исправлено фазой D|Уточнено фазой D|ИСПРАВЛЕНО фазой D|CORRECTED[^\]]*)\]"
)
TAG_CLASS = {
    "verified": "ok",
    "confirmed-real": "ok",
    "hypothesis": "warn",
    "speculative": "warn",
    "weak": "warn",
    "inferred": "warn",
    "needs-real-data": "warn",
    "falsified": "bad",
    "weakened": "warn",
    "unknown": "bad",
    "conflicting": "bad",
}


def tag_class(word: str) -> str:
    w = word.lower()
    if w.startswith("исправлено") or w.startswith("уточнено") or w.startswith("corrected"):
        return "warn"
    for key, cls in TAG_CLASS.items():
        if w.startswith(key):
            return cls
    return "warn"


def wrap_tags(htmltext: str) -> str:
    def repl(m: re.Match) -> str:
        word = m.group(1)
        return f'<span class="tag tag-{tag_class(word)}">{word}</span>'

    return TAG_RE.sub(repl, htmltext)


TABLE_RE = re.compile(r"<table>.*?</table>", re.DOTALL)


def wrap_tables(htmltext: str) -> str:
    return TABLE_RE.sub(lambda m: f'<div class="table-wrap">{m.group(0)}</div>', htmltext)


def render_md(path: Path) -> str:
    MD.reset()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = "\n".join(lines)
    out = MD.convert(body)
    return wrap_tables(wrap_tags(out))


def fig_html(slug: str) -> str:
    data = (FIG / f"{slug}.png").read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    cap = FIG_CAPTIONS[slug]
    return (
        '<figure class="chart">'
        f'<img src="data:image/png;base64,{b64}" alt="{html.escape(cap)}" loading="lazy">'
        f"<figcaption>{html.escape(cap)}</figcaption>"
        "</figure>"
    )


def chapter_title(fname: str) -> tuple[str, str]:
    num = fname.split("-", 1)[0]
    first_line = (CH / fname).read_text(encoding="utf-8").splitlines()[0]
    title = first_line.lstrip("#").strip()
    if "—" in title:
        title = title.split("—", 1)[1].strip()
    return num, title


sections_html = []
nav_html = []

for part_num, part_title, part_dates, chapters in PARTS:
    part_id = f"part-{part_num}"
    nav_html.append(
        f'<div class="nav-part"><span class="nav-part-label">Часть {part_num}</span>'
        f'<a href="#{part_id}" class="nav-part-title">{html.escape(part_title)}</a><ul>'
    )
    sections_html.append(
        f'<section class="part-divider" id="{part_id}">'
        f'<div class="part-num">Часть {part_num}</div>'
        f"<h2>{html.escape(part_title)}</h2>"
        f'<div class="part-dates">{html.escape(part_dates)}</div>'
        "</section>"
    )
    for fname, figs in chapters:
        num, title = chapter_title(fname)
        ch_id = f"ch-{num}"
        nav_html.append(
            f'<li><a href="#{ch_id}"><span class="nav-num">{num}</span>{html.escape(title)}</a></li>'
        )
        body = render_md(CH / fname)
        figures_block = ""
        if figs:
            fig_list = figs if isinstance(figs, list) else [figs]
            figures_block = "".join(fig_html(f) for f in fig_list)
        sections_html.append(
            f'<article class="chapter" id="{ch_id}">'
            f'<div class="chapter-eyebrow">Часть {part_num}</div>'
            f'<h3><span class="ch-num">{num}</span>{html.escape(title)}</h3>'
            f'<div class="chapter-body">{body}</div>'
            f"{figures_block}"
            "</article>"
        )
    nav_html.append("</ul></div>")

# Appendix: full chronology
chrono_path = ROOT / "01_CHRONOLOGY.md"
chrono_html = render_md(chrono_path) if chrono_path.exists() else ""

nav_html.append(
    '<div class="nav-part"><span class="nav-part-label">Приложение</span>'
    '<a href="#appendix-chrono" class="nav-part-title">Полная хронология</a></div>'
)

sections_html.append(
    '<section class="part-divider" id="appendix">'
    '<div class="part-num">Приложение</div>'
    "<h2>Полная хронология</h2>"
    '<div class="part-dates">из git log, фаза A</div>'
    "</section>"
)
sections_html.append(
    f'<article class="chapter" id="appendix-chrono">'
    f'<div class="chapter-body">{chrono_html}</div>'
    "</article>"
)

BODY_SECTIONS = "\n".join(sections_html)
NAV = "\n".join(nav_html)

TEMPLATE = (RENDER_DIR / "book_template.html").read_text(encoding="utf-8")

final = TEMPLATE.replace("{{NAV}}", NAV).replace("{{SECTIONS}}", BODY_SECTIONS)
OUT.write_text(final, encoding="utf-8")
print("Wrote", OUT, len(final), "chars")
