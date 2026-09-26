#!/usr/bin/env python3
"""HTML -> Letter PDF for the son 500 and 1000 Gladius play packs.

PDFs are gitignored. Prefer (in order):
  1. C:\\Personal\\print_aids\\40k_11e  (owner Windows path)
  2. ~/print_aids/40k_11e
  3. /opt/cursor/artifacts/print_aids_40k_11e  (cloud agent download folder)

Uses Playwright Chromium when available; otherwise Google Chrome headless.
"""
from __future__ import annotations

import asyncio
import os
import shutil
import subprocess
import sys
from pathlib import Path

HTML_DIR = Path(__file__).resolve().parent

AIDS = [
    "40k_sm_army_list_500",
    "40k_sm_how_army_works_500",
    "40k_sm_army_list_1000",
    "40k_sm_how_army_works_1000",
    "40k_11e_cheat_sheet_wounds",
]


def resolve_pdf_dirs() -> list[Path]:
    dirs: list[Path] = []
    win = Path(r"C:\Personal\print_aids\40k_11e")
    if win.parent.exists() or os.name == "nt":
        dirs.append(win)
    dirs.append(Path.home() / "print_aids" / "40k_11e")
    cloud = Path("/opt/cursor/artifacts/print_aids_40k_11e")
    if cloud.parent.is_dir():
        dirs.append(cloud)
    # de-dupe while preserving order
    seen: set[Path] = set()
    out: list[Path] = []
    for d in dirs:
        r = d.resolve() if d.exists() else d
        if r not in seen:
            seen.add(r)
            out.append(d)
    return out


def chrome_bin() -> str | None:
    for name in ("google-chrome", "chromium", "chromium-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    if os.name == "nt":
        candidates = [
            Path(os.environ.get("PROGRAMFILES", "")) / "Google/Chrome/Application/chrome.exe",
            Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Google/Chrome/Application/chrome.exe",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Google/Chrome/Application/chrome.exe",
            Path(os.environ.get("PROGRAMFILES", "")) / "Microsoft/Edge/Application/msedge.exe",
            Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Microsoft/Edge/Application/msedge.exe",
        ]
        for candidate in candidates:
            if candidate.is_file():
                return str(candidate)
    return None


def render_chrome(html_path: Path, pdf_path: Path, chrome: str) -> None:
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    # Unique profile avoids SingletonLock races; timeout because headless
    # Chrome often hangs after writing the PDF in this environment.
    # Delete a stale PDF first so a timeout cannot report the old file as success.
    import tempfile
    import time

    if pdf_path.is_file():
        try:
            pdf_path.unlink()
        except PermissionError:
            raise RuntimeError(
                f"LOCKED (close it in your PDF viewer and re-run): {pdf_path}"
            ) from None
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
            subprocess.run(cmd, check=False, capture_output=True, timeout=90)
        except subprocess.TimeoutExpired:
            # PDF is usually already on disk when Chrome stalls after write.
            pass
        # Brief settle for filesystem flush
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
        # prefer_css_page_size: honour @page { size: letter; margin: ... }
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
        print(
            "Need playwright or google-chrome.\n"
            "  pip install playwright && playwright install chromium\n"
            "  — or install Google Chrome / Chromium.",
            file=sys.stderr,
        )
        return 1

    failures = 0
    for name in AIDS:
        html_path = HTML_DIR / f"{name}.html"
        if not html_path.is_file():
            print(f"MISSING HTML: {html_path}", file=sys.stderr)
            return 1
        pdf_path = primary / f"{name}.pdf"
        if use_playwright:
            await render_playwright(html_path, pdf_path)
        else:
            assert chrome is not None
            try:
                render_chrome(html_path, pdf_path, chrome)
            except RuntimeError as exc:
                print(f"FAIL {exc}", file=sys.stderr)
                failures += 1
                continue
        print(f"OK {pdf_path} ({pdf_path.stat().st_size} bytes)")

        # Mirror into other output dirs (cloud artifacts, etc.)
        for extra in pdf_dirs[1:]:
            if extra.resolve() == primary.resolve():
                continue
            extra.mkdir(parents=True, exist_ok=True)
            dest = extra / f"{name}.pdf"
            shutil.copy2(pdf_path, dest)
            print(f"   copy -> {dest}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
