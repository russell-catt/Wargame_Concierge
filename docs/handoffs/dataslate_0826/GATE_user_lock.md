# GATE — User lock (dataslate_0826)

**Track:** `dataslate_0826`  
**Branch:** `feature/dataslate_0826`  
**Date opened:** 2026-08-27

## Blockers before full execution

| # | Gate | Status |
|---|------|--------|
| G1 | WarCom egress / pastes / uploads / Drive | **Partial** — pastes + Universal Rules PDF; **Drive folder linked but unreachable** ([`research/gdrive_40k_dataslates.md`](research/gdrive_40k_dataslates.md)) |
| G2 | Owner confirms PDFs saved under `C:\Personal\40K\rules\` (or accepts `draft`) | Open — also save Drive folder copies locally |
| G3 | Owner authorizes multi-slice execution | Open |
| G3b | Optional: authorize **S2b** / **S2c** / **S2d** / **S2e** before full track | Open |
| G1d | Unblock Drive **or** upload KT dataslate (+ new 40K files) | **Open** — owner added KT dataslate to Drive; agent still cannot read folder |

## Authorize by saying

> Authorize dataslate_0826 — run S0 through FS on `feature/dataslate_0826`.

Optional paste format if egress blocked:

```text
L1: <title> | <canonical URL> | <date> | <PDF name>
L2: ...
L3: ...
Local 40K path: C:\Personal\40K\rules\<file>
Local KT path: C:\Personal\Kill Team\kill_team_2024\<file>
```
