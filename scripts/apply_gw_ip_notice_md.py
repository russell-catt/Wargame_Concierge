#!/usr/bin/env python3
"""Add ## Games Workshop notice to Tier B games/ markdown (gw_community_content S3)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GAMES = ROOT / "games"

NOTICE_40K = """## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Warhammer 40,000 and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Warhammer 40,000 is Copyright Games Workshop Limited. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

"""

NOTICE_KT = """## Games Workshop notice

**UNOFFICIAL.** This document is completely unofficial and in no way endorsed by Games Workshop Limited. Personal / no-charge use only — never for sale. Warhammer, Kill Team and associated marks are trademarks of Games Workshop Limited. Used without permission. No challenge to their status intended. Kill Team is Copyright Games Workshop Limited 2024. Teaching notes by Russell Catt (Wargame Concierge). Games Workshop retains IP in the settings and characters. No official logos.

"""

SKIP_PARTS = (
    "/units/research/",
    "/cards/",
    "/operatives/",
)

TIER_B_NAME_PARTS = (
    "README.md",
    "Starter_",
    "Army_List_",
    "Quick_Reference",
    "Reference_Guide",
    "Owned_Models",
    "Event_Ready",
    "Turn_Structure",
    "Key_Concepts",
    "Board_Setup",
    "Terrain_",
    "Chapter_Approved",
    "Cryptek_Conclave",
    "Gladius_",
    "Oath_of_Moment",
    "First_Company",
    "Anvil_",
    "Core_Rules_Quotes",
    "Target_Eligibility",
    "Patch_Manifest",
    "Keyword_Glossary",
    "Overview.md",
    "Team_Rule_Guide",
    "Volkus_Playbook",
    "Starter_Roster",
    "starter_set",
    "Starter_Forces",
    "Learn_to_Play",
    "Mission_Packs",
    "How_To_Create",
    "Custom_Builder",
    "Necron_Lists",
    "Unit_Index",
    "Operatives_Index",
)


def is_tier_b(path: Path) -> bool:
    rel = path.as_posix()
    if any(s in rel for s in SKIP_PARTS):
        return False
    if path.name == "README.md":
        return True
    return any(p in path.name for p in TIER_B_NAME_PARTS)


def notice_for(path: Path) -> str:
    if "kill_team_2024" in path.as_posix():
        return NOTICE_KT
    if "warhammer_40k_11e" in path.as_posix():
        return NOTICE_40K
    # games/README.md — both systems
    return NOTICE_40K.replace(
        "Warhammer 40,000 is Copyright",
        "Warhammer 40,000 and Kill Team are Copyright Games Workshop Limited (Kill Team 2024 where applicable). Warhammer 40,000 is Copyright",
    )


def insert_notice(text: str, notice: str) -> str:
    if "## Games Workshop notice" in text:
        return text
    # Before Change Log
    if "## Change Log" in text:
        return text.replace("## Change Log", notice + "## Change Log", 1)
    # Before Rising Tide footer markers
    if "## Rising Tide Notes" in text:
        return text.replace("## Rising Tide Notes", notice + "## Rising Tide Notes", 1)
    if "## Attribution" in text and "## Change Log" not in text:
        return text.replace("## Attribution", notice + "## Attribution", 1)
    return text.rstrip() + "\n\n---\n\n" + notice


def main() -> None:
    updated = []
    for md in sorted(GAMES.rglob("*.md")):
        if not is_tier_b(md):
            continue
        text = md.read_text(encoding="utf-8")
        new = insert_notice(text, notice_for(md))
        if new != text:
            md.write_text(new, encoding="utf-8", newline="\n")
            updated.append(md.relative_to(ROOT))
    print(f"Updated {len(updated)} markdown files:")
    for p in updated:
        print(f"  {p}")


if __name__ == "__main__":
    main()
