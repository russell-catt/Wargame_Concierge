#!/usr/bin/env python3
"""HTML -> PDF for learn_to_play_event S6 KT print aids. PDFs outside the repo."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

HTML_DIR = Path(__file__).resolve().parent
PDF_DIR = Path(r"C:\Personal\print_aids\learn_to_play_event")

AIDS = [
    "kt_shared_turn_structure",
    "kt_shared_volkus_terrain",
    "kt_shared_target_eligibility",
    "kt_pm_quick_reference",
    "kt_pm_volkus_playbook",
    "kt_pm_starter_roster",
    "kt_pm_faction_rules",
    "kt_kommandos_quick_reference",
    "kt_kommandos_volkus_playbook",
    "kt_kommandos_starter_roster",
    "kt_kommandos_faction_rules",
]


async def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("playwright not installed", file=sys.stderr)
        return 1

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        for name in AIDS:
            html_path = HTML_DIR / f"{name}.html"
            pdf_path = PDF_DIR / f"{name}.pdf"
            if not html_path.is_file():
                print(f"MISSING HTML: {html_path}", file=sys.stderr)
                await browser.close()
                return 1
            await page.goto(html_path.as_uri(), wait_until="networkidle")
            await page.pdf(
                path=str(pdf_path),
                format="Letter",
                landscape=("target_eligibility" in name),
                margin={
                    "top": "0.5in",
                    "right": "0.5in",
                    "bottom": "0.5in",
                    "left": "0.5in",
                },
                print_background=True,
                prefer_css_page_size=True,
            )
            print(f"OK {pdf_path.name}")
        await browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
