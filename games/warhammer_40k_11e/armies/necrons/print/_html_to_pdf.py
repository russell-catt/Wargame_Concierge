#!/usr/bin/env python3
"""HTML -> Letter PDF for Necron / Cryptek print aids.

PDFs are gitignored. Prefer (in order):
  1. C:\\Personal\\print_aids\\40k_11e
  2. C:\\Personal\\print_aids\\learn_to_play_event  (legacy 250 bag)
  3. ~/print_aids/40k_11e
  4. /opt/cursor/artifacts/print_aids_40k_11e

Uses Playwright when available; otherwise Google Chrome headless.
"""
from __future__ import annotations

import asyncio
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HTML_DIR = Path(__file__).resolve().parent

# Cryptek 500 play pack first; then legacy 250 / event bag aids
AIDS = [
    "40k_roster_500_conclave",
    "40k_how_army_works_500_conclave",
    "40k_conclave_primary_missions",
    "40k_roster_250_conclave",
    "40k_reference_250_conclave",
    "40k_necrons_quick_reference",
    "40k_first_game_core",
    "40k_setup_terrain",
]


def resolve_pdf_dirs() -> list[Path]:
    dirs: list[Path] = []
    for candidate in (
        Path(r"C:\Personal\print_aids\40k_11e"),
        Path(r"C:\Personal\print_aids\learn_to_play_event"),
        Path.home() / "print_aids" / "40k_11e",
        Path("/opt/cursor/artifacts/print_aids_40k_11e"),
    ):
        if candidate.as_posix().startswith("C:") and os.name != "nt":
            if not candidate.parent.exists():
                continue
        if candidate.parent.is_dir() or candidate.as_posix().startswith("/opt/cursor"):
            dirs.append(candidate)
        elif candidate == Path.home() / "print_aids" / "40k_11e":
            dirs.append(candidate)
    # Always include home + cloud
    for extra in (Path.home() / "print_aids" / "40k_11e", Path("/opt/cursor/artifacts/print_aids_40k_11e")):
        if extra not in dirs:
            dirs.append(extra)
    seen: set[str] = set()
    out: list[Path] = []
    for d in dirs:
        key = str(d)
        if key not in seen:
            seen.add(key)
            out.append(d)
    return out


def chrome_bin() -> str | None:
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    return None


def render_chrome(html_path: Path, pdf_path: Path, chrome: str) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="chrome-pdf-") as prof:
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--no-pdf-header-footer",
            f"--user-data-dir={prof}",
            f"--print-to-pdf={pdf_path}",
            html_path.as_uri(),
        ]
        try:
            subprocess.run(cmd, check=False, capture_output=True, timeout=45)
        except subprocess.TimeoutExpired:
            pass
        for _ in range(20):
            if pdf_path.is_file() and pdf_path.stat().st_size > 1000:
                return
            time.sleep(0.25)
        raise RuntimeError(f"Chrome did not produce PDF: {pdf_path}")


async def render_playwright(html_path: Path, pdf_path: Path) -> None:
    from playwright.async_api import async_playwright

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(html_path.as_uri(), wait_until="networkidle")
        await page.pdf(
            path=str(pdf_path),
            format="Letter",
            print_background=True,
            prefer_css_page_size=True,
        )
        await browser.close()


async def main() -> int:
    pdf_dirs = resolve_pdf_dirs()
    primary = pdf_dirs[0]
    primary.mkdir(parents=True, exist_ok=True)

    use_playwright = False
    try:
        import playwright  # noqa: F401

        use_playwright = True
    except ImportError:
        pass

    chrome = chrome_bin()
    if not use_playwright and not chrome:
        print("Need playwright or google-chrome.", file=sys.stderr)
        return 1

    for name in AIDS:
        html_path = HTML_DIR / f"{name}.html"
        if not html_path.is_file():
            print(f"SKIP missing HTML: {html_path}", file=sys.stderr)
            continue
        pdf_path = primary / f"{name}.pdf"
        if use_playwright:
            await render_playwright(html_path, pdf_path)
        else:
            assert chrome is not None
            render_chrome(html_path, pdf_path, chrome)
        print(f"OK {pdf_path} ({pdf_path.stat().st_size} bytes)")
        for extra in pdf_dirs[1:]:
            if extra.resolve() == primary.resolve():
                continue
            extra.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf_path, extra / f"{name}.pdf")
            print(f"   copy → {extra / (name + '.pdf')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
