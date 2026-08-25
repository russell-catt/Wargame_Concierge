#!/usr/bin/env python3
"""HTML -> PDF for 40K setup print aids. PDFs land outside the repo."""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

HTML_DIR = Path(__file__).resolve().parent
PDF_DIR = Path(r"C:\Personal\print_aids\40k_11e")

AIDS = [
    "40k_wound_roll_reference",
    "40k_wd527_mission",
    "40k_chapter_approved_force_dispositions",
    "40k_system_quick_reference",
]


async def main() -> int:
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print(
            "playwright not installed; try: pip install playwright && playwright install chromium",
            file=sys.stderr,
        )
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
            uri = html_path.as_uri()
            await page.goto(uri, wait_until="networkidle")
            await page.pdf(
                path=str(pdf_path),
                format="Letter",
                margin={
                    "top": "0.5in",
                    "right": "0.5in",
                    "bottom": "0.5in",
                    "left": "0.5in",
                },
                print_background=True,
                prefer_css_page_size=True,
            )
            print(f"OK {pdf_path}")
        await browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
