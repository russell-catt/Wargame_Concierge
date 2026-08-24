#!/usr/bin/env python3
"""Apply GW unofficial banner + footer to games/**/*.html (track gw_community_content S1)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAMES = ROOT / "games"

GW_CSS = """
.gw-ip-banner {
  font-size: 9pt;
  font-weight: 600;
  border: 2px solid #333;
  padding: 0.35em 0.5em;
  margin: 0 0 0.5em;
  background: #f5f5f5;
}
.gw-ip-footer {
  font-size: 7pt;
  color: #444;
  margin-top: 0.5em;
  border-top: 1px solid #999;
  padding-top: 0.25em;
  line-height: 1.25;
}
""".strip()

BANNER = (
    '<p class="gw-ip-banner"><strong>UNOFFICIAL</strong> — fan teaching material, '
    "not a Games Workshop product, not endorsed by Games Workshop Limited.</p>"
)

FOOTER_40K = (
    "<strong>UNOFFICIAL.</strong> This document is completely unofficial and in no way "
    "endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. "
    "Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. "
    "Used without permission. No challenge to their status intended. "
    "Warhammer 40,000 is Copyright Games Workshop Limited. "
    "Teaching notes by Russell Catt (Wargame Concierge). "
    "Games Workshop retains IP in the settings and characters. No official logos."
)

FOOTER_KT = (
    "<strong>UNOFFICIAL.</strong> This document is completely unofficial and in no way "
    "endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. "
    "Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. "
    "Used without permission. No challenge to their status intended. "
    "Kill Team is Copyright Games Workshop Limited 2024. "
    "Teaching notes by Russell Catt (Wargame Concierge). "
    "Games Workshop retains IP in the settings and characters. No official logos."
)

CARD_FT_SUFFIX = (
    " · UNOFFICIAL · not endorsed by Games Workshop Limited · personal use only · "
    "© Games Workshop Limited 2024"
)


def is_card(path: Path) -> bool:
    return "/cards/" in path.as_posix().replace("\\", "/")


def is_kt(path: Path) -> bool:
    return "kill_team_2024" in path.as_posix()


def inject_css(text: str) -> str:
    if ".gw-ip-banner" in text:
        return text
    return text.replace("</style>", GW_CSS + "\n</style>", 1)


def inject_banner(text: str) -> str:
    if "gw-ip-banner" in text:
        return text
    # After first <body> or <body ...>
    m = re.search(r"(<body[^>]*>\s*)", text, re.I)
    if not m:
        return text
    insert_at = m.end()
    # Prefer inside first .page section if present
    page_m = re.search(r'(<section\s+class="page">\s*)', text[insert_at:], re.I)
    if page_m:
        insert_at += page_m.end()
    return text[:insert_at] + "\n  " + BANNER + "\n" + text[insert_at:]


def page_suffix(old_inner: str) -> str:
    m = re.search(r"( Page \d+ of \d+.*)$", old_inner.strip())
    return m.group(1) if m else ""


def replace_footers(text: str, footer_body: str) -> str:
    def repl(match: re.Match[str]) -> str:
        suffix = page_suffix(match.group(1))
        return f'<p class="gw-ip-footer">{footer_body}{suffix}</p>'

    text = re.sub(
        r'<p class="footer"[^>]*>(.*?)</p>',
        repl,
        text,
        flags=re.S,
    )
    # Target eligibility uses multiline footer with class footer
    if "gw-ip-footer" not in text and 'class="footer"' in text:
        text = re.sub(
            r'<p class="footer">\s*(.*?)\s*</p>',
            repl,
            text,
            flags=re.S,
        )
    return text


def update_card(text: str) -> str:
    if "UNOFFICIAL · not endorsed" in text:
        return text
    # Replace Personal use only segment in .ft
    text = re.sub(
        r"(<div class=ft>.*?)( · Personal use only)( · Source:.*?)(</div>)",
        r"\1" + CARD_FT_SUFFIX + r"\3\4",
        text,
        flags=re.S,
    )
    if "UNOFFICIAL · not endorsed" not in text:
        text = re.sub(
            r"(<div class=ft>)([^<]+)(</div>)",
            lambda m: m.group(1)
            + m.group(2).rstrip()
            + CARD_FT_SUFFIX
            + m.group(3),
            text,
            count=1,
        )
    return text


def update_te_footer(text: str) -> str:
    """Target Eligibility cheat sheet — preserve attribution tail after GW block."""
    if "gw-ip-footer" in text:
        return text
    footer_match = re.search(r'<p class="footer">\s*(.*?)\s*</p>', text, re.S)
    if not footer_match:
        return text
    old = footer_match.group(1)
    # Keep non-GW attribution after first sentence block
    tail_parts = []
    if "Full quote appendix" in old:
        idx = old.find("Full quote appendix")
        tail_parts.append(old[idx:])
    elif "Layout inspiration" in old:
        idx = old.find("Layout inspiration")
        tail_parts.append(old[idx:])
    tail = " " + " ".join(tail_parts) if tail_parts else ""
    quote_note = (
        " Verbatim lines are from owned local PDFs for personal table use; "
        "they are not a substitute for official publications and must not be redistributed."
    )
    new_footer = (
        f'<p class="gw-ip-footer">{FOOTER_KT}{quote_note}{tail}</p>'
    )
    return text[: footer_match.start()] + new_footer + text[footer_match.end() :]


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    if is_card(path):
        text = update_card(text)
    else:
        footer_body = FOOTER_KT if is_kt(path) else FOOTER_40K
        text = inject_css(text)
        text = inject_banner(text)
        if "Target_Eligibility" in path.name:
            text = update_te_footer(text)
        else:
            text = replace_footers(text, footer_body)

    if text != original:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main() -> None:
    updated = []
    for html in sorted(GAMES.rglob("*.html")):
        if process_file(html):
            updated.append(html.relative_to(ROOT))
    print(f"Updated {len(updated)} HTML files:")
    for p in updated:
        print(f"  {p}")


if __name__ == "__main__":
    main()
