# Source ledger — Warcode Kickstarter refresh

Retrieved 2026-09-24 unless otherwise stated.

| ID | Source | Provenance | SHA-256 / state | Authority and handling |
|---|---|---|---|---|
| WCR-089 | `raw/the_warcode/The-Warcode-Rulebook-V.0.8.9-F.pdf` | Free download linked from Kickstarter; local acquisition path recorded in pointer | `4dc9efc7d97b7c14ce4f1afa729d8b0dd2fa97a51fa2d1b8385003ea75c1c93d` | Current mechanics baseline; 41 pages |
| WCL-FE | `raw/the_warcode/The-Warcode-Lorebook-Tactical-Doctrine-Field-Edition.pdf` | Free download linked from Kickstarter; local acquisition path recorded in pointer | `9e79454440c0e50d228969dd10e7f2c39c4e1b3821d8b26587b0fb35764ec244` | Narrative source only; 40 pages; metadata date 2026-09-15 |
| WCR-087 | `raw/the_warcode/The Warcode Rulebook V.0.8.7-F.pdf` | Previous free beta | Historical | Retained for delta/provenance; superseded on the same topic |
| GF-2026 | https://gamefound.com/en/projects/redmakers/the-warcode | Public campaign page | Cancelled; platform states no funds collected | Historical campaign facts; timestamp volatile metrics |
| KS-2026 | https://www.kickstarter.com/projects/redmakers/the-warcode-stl-campaign | Public campaign page | Live 2026-09-23 through 2026-10-23 | Current digital-only offer; timestamp volatile metrics |
| PRE-2026 | https://pre-launch.thewarcode.com/ | Publisher pre-launch site | Historical marketing | Secondary to current PDFs; contradictions retained |
| TTS | Steam Workshop listing for The Warcode | Public playable mod | Listing still labels v0.8.7 | Version-drift warning |

## Version hierarchy

1. Rulebook v0.8.9-F is the current mechanics source.
2. Rulebook v0.8.7-F remains historical evidence. It controls only where a
   later source does not address the topic; omission is not a patch.
3. The Tactical Doctrine Field Edition is narrative context, never mechanics
   authority.
4. Publisher campaign pages establish offer and publisher-claim facts, not
   independent proof of campaign causation or success.

## Extraction record

- `rulebook_v089f_extract.txt`: native text with explicit PDF-page markers.
  Cover p.1 and trailing art p.41 contain no native text.
- `lorebook_tactical_doctrine_field_edition_extract.txt`: native text with
  explicit PDF-page markers. Cover p.1 contains no native text.
- No new OCR sidecar was required. Existing v0.8.7 contract/protocol/map
  sidecars remain valid after source-page equivalence is verified.
