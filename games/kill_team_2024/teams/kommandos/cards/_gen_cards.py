"""Generate Kommandos HTML datacards from owned Teams PDF extract (2026-08-21)."""
from pathlib import Path

OUT = Path(r"C:\Personal\Personal_Projects\Wargame_Concierge\games\kill_team_2024\teams\kommandos\cards")
CSS = """@page { size: 90mm 63mm; margin: 4mm; }
* { box-sizing: border-box; }
body { font-family: Segoe UI, Arial, sans-serif; font-size: 7pt; margin: 0; color: #111; }
.card { border: 2px solid #1a1a1a; padding: 4px; height: 55mm; display: flex; flex-direction: column; }
.hdr { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 2px solid #2d6a2d; padding-bottom: 2px; margin-bottom: 3px; }
.name { font-size: 10pt; font-weight: 700; color: #2d6a2d; text-transform: uppercase; }
.stats { display: flex; gap: 6px; font-size: 7pt; font-weight: 600; }
.stats span { background: #eee; padding: 1px 4px; border-radius: 2px; }
table { width: 100%; border-collapse: collapse; font-size: 6pt; margin: 2px 0; }
th { background: #2d6a2d; color: #fff; padding: 1px 2px; text-align: left; }
td { border-bottom: 1px solid #ccc; padding: 1px 2px; vertical-align: top; }
.rules { font-size: 5.5pt; flex: 1; overflow: hidden; line-height: 1.15; }
.rules p { margin: 1px 0; }
.ft { font-size: 5pt; color: #555; border-top: 1px solid #aaa; margin-top: auto; padding-top: 2px; }
@media print { body { -webkit-print-color-adjust: exact; print-color-adjust: exact; } }"""

# name, file, apl, move, save, wounds, base, weapons[(n,atk,hit,dmg,wr)], rules, keywords
CARDS = [
    ("Boss Nob", "Boss_Nob.html", 3, '6"', "5+", 14, "32",
     [("Slugga", "4", "4+", "3/4", 'Range 8"'),
      ("Big choppa", "5", "3+", "5/6", "-"),
      ("Power klaw", "4", "3+", "5/7", "Brutal, Shock")],
     "<p><strong>Krumpin' Time</strong> Two Fight actions per activation.</p><p><strong>Get It Dun!</strong> 1AP SUPPORT: +1 APL to another KOMMANDO (not Squig) within 6\".</p>",
     "KOMMANDO, ORK, LEADER, BOSS NOB"),
    ("Boy", "Boy.html", 2, '6"', "5+", 10, "32",
     [("Slugga", "4", "4+", "3/4", 'Range 8"'), ("Choppa", "4", "3+", "4/5", "-")],
     "<p><strong>Taktical Wot-notz</strong> Once per TP: one Boy Smoke Grenade; one Boy Stun Grenade (does not count toward equipment limits).</p>",
     "KOMMANDO, ORK, BOY"),
    ("Bomb Squig", "Bomb_Squig.html", 2, '6"', "5+", 5, "25",
     [("Explosives", "6", "4+", "4/5", 'Blast 1", Limited 1, Explosive*'), ("Bite", "3", "4+", "4/5", "-")],
     "<p><strong>Explosive*</strong> Shoot while in enemy control range; self is primary target.</p><p><strong>Boom!</strong> On incap before using explosives: roll; on 4+ free Shoot with explosives.</p><p><strong>Stoopid / Expendable</strong> See PDF — no Conceal; limited actions; ignored for kill/escape scoring.</p>",
     "KOMMANDO, ORK, BOMB SQUIG"),
    ("Breacha Boy", "Breacha_Boy.html", 2, '6"', "5+", 10, "32",
     [("Slugga", "4", "4+", "3/4", 'Range 8"'), ("Breacha ram", "4", "4+", "5/5", "Brutal, Severe, Shock")],
     "<p><strong>Breach</strong> 1AP: place Breach marker; treat thin terrain as Accessible. Can do during Charge/Reposition for 1 less AP.</p>",
     "KOMMANDO, ORK, BREACHA BOY"),
    ("Burna Boy", "Burna_Boy.html", 2, '6"', "5+", 10, "32",
     [("Burna (standard)", "4", "2+", "3/3", 'Range 8", Saturate, Torrent 2"'),
      ("Burna (deluge)", "4", "2+", "3/3", 'Range 4", Saturate, Seek, Torrent 0"'),
      ("Fists", "3", "3+", "3/4", "-")],
     "<p>Torrent 0\" = no secondary targets but still counts as Torrent (e.g. Condensed Stronghold).</p>",
     "KOMMANDO, ORK, BURNA BOY"),
    ("Comms Boy", "Comms_Boy.html", 2, '6"', "5+", 10, "32",
     [("Shokka pistol", "6", "4+", "1/0", 'Range 8", Devastating 2, Severe, Stun'), ("Fists", "3", "3+", "3/4", "-")],
     "<p><strong>I Got a Plan, Ladz</strong> Once per activation: Pick Up / Place Marker or mission action for 1 less AP.</p><p><strong>Listen In</strong> 1AP SUPPORT: +1 APL to another KOMMANDO (not Squig) within 6\".</p>",
     "KOMMANDO, ORK, COMMS BOY"),
    ("Dakka Boy", "Dakka_Boy.html", 2, '6"', "5+", 10, "32",
     [("Dakka shoota (short)", "5", "4+", "3/4", 'Range 9", Ceaseless'),
      ("Dakka shoota (long)", "5", "4+", "3/4", "-"),
      ("Fists", "3", "3+", "3/4", "-")],
     "<p><strong>Dakka Dash</strong> 1AP: free Dash + free Shoot with dakka shoota (not Conceal; not in enemy control range).</p>",
     "KOMMANDO, ORK, DAKKA BOY"),
    ("Grot", "Grot.html", 2, '6"', "5+", 5, "25",
     [("Grot choppa", "3", "5+", "1/4", "-")],
     "<p><strong>Sneaky Zogger</strong> Cannot Engage. In cover: cannot be valid target (precedence) except within 2\".</p><p><strong>Grappling Hook</strong> 1AP reposition onto visible terrain point.</p>",
     "KOMMANDO, ORK, GROT"),
    ("Rokkit Boy", "Rokkit_Boy.html", 2, '6"', "5+", 10, "32",
     [("Rokkit (aimed)", "6", "4+", "4/5", 'Blast 1", Ceaseless, Heavy (Dash only)'),
      ("Rokkit (mobile)", "6", "4+", "4/5", 'Blast 1"'),
      ("Fists", "3", "3+", "3/4", "-")],
     "<p>Aimed profile needs Heavy (Dash only) restrictions.</p>",
     "KOMMANDO, ORK, ROKKIT BOY"),
    ("Slasha Boy", "Slasha_Boy.html", 2, '6"', "5+", 10, "32",
     [("Throwing knives", "4", "3+", "2/5", 'Range 6", Silent'),
      ("Twin choppas", "4", "3+", "4/5", "Ceaseless, Lethal 5+")],
     "<p><strong>Dat All You Got?</strong> After fight/retaliate if not incapacitated: D3 damage to that enemy.</p>",
     "KOMMANDO, ORK, SLASHA BOY"),
    ("Snipa Boy", "Snipa_Boy.html", 2, '6"', "5+", 10, "32",
     [("Scoped big shoota (concealed)", "5", "3+", "3/3", "Devastating 2, Heavy, Silent, Concealed Position*"),
      ("Scoped big shoota (stationary)", "5", "3+", "3/3", "Devastating 2, Heavy"),
      ("Scoped big shoota (sweeping)", "5", "3+", "3/4", 'Heavy (Dash only), Torrent 1"'),
      ("Fists", "3", "3+", "3/4", "-")],
     "<p><strong>Concealed Position</strong> Concealed profile only the first Shoot of the battle.</p>",
     "KOMMANDO, ORK, SNIPA BOY"),
]

def card_html(c):
    name, fname, apl, move, save, w, base, weapons, rules, kw = c
    rows = "".join(f"<tr><td>{n}</td><td>{a}</td><td>{h}</td><td>{d}</td><td>{wr}</td></tr>" for n,a,h,d,wr in weapons)
    return f"""<!DOCTYPE html><html><head><meta charset=utf-8><title>{name}</title><style>
{CSS}
</style></head><body>
<div class=card>
<div class=hdr><div class=name>{name}</div><div class=stats>
<span>APL {apl}</span><span>MOVE {move}</span><span>SAVE {save}</span><span>W {w}</span>
</div></div>
<table><tr><th>Weapon</th><th>ATK</th><th>HIT</th><th>DMG</th><th>WR</th></tr>{rows}</table>
<div class=rules>{rules}</div>
<div class=ft>{kw} · {base}mm · Personal use only · Source: eng_17-06 Kommandos Teams PDF 2026-08-21</div>
</div></body></html>"""

for c in CARDS:
    path = OUT / c[1]
    path.write_text(card_html(c), encoding="utf-8")
    print("wrote", path.name)
print("done", len(CARDS))
