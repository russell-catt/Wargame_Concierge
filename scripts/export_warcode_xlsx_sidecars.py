#!/usr/bin/env python3
"""Export Warcode contract/protocol xlsx to UTF-8 sidecars."""
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XLSX = ROOT / "raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx"
NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"


def read_xlsx_sheets(xlsx_path: Path):
    with zipfile.ZipFile(xlsx_path) as z:
        ss = ET.fromstring(z.read("xl/sharedStrings.xml"))
        strings = []
        for si in ss.findall("m:si", NS):
            parts = []
            for t in si.iter("{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t"):
                if t.text:
                    parts.append(t.text)
            strings.append("".join(parts))
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        rid_to_target = {r.get("Id"): r.get("Target") for r in rels}
        sheets = []
        for s in wb.findall(".//m:sheet", NS):
            name = s.get("name")
            rid = s.get(f"{{{REL_NS}}}id")
            target = rid_to_target[rid]
            ws_path = (
                "xl/" + target
                if target.startswith("worksheets/")
                else f"xl/worksheets/{target.split('/')[-1]}"
            )
            ws = ET.fromstring(z.read(ws_path))
            rows = []
            for row in ws.findall(".//m:sheetData/m:row", NS):
                cells = []
                for c in row.findall("m:c", NS):
                    t = c.get("t")
                    v = c.find("m:v", NS)
                    if v is None:
                        continue
                    val = strings[int(v.text)] if t == "s" else v.text
                    cells.append(val)
                if cells:
                    rows.append(cells)
            sheets.append((name, rows))
        return sheets


def main():
    sheets = read_xlsx_sheets(XLSX)
    out_c = ROOT / "raw/the_warcode/contract_cards_transcription.txt"
    lines = [
        "# Contract Cards transcription — The Warcode Rulebook V.0.8.7-F",
        "",
        "**Source:** raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx — Contracts sheet",
        "**Method:** via typed transcription (owner spreadsheet)",
        "**Confidence:** draft",
        "**Date:** 2026-08-25",
        "",
        'Standard boilerplate on every card: "You have received a contract. Eliminate the target designated by enemy faction."',
        "All cards award **1 VP** on fulfilment.",
        "",
    ]
    for name, rows in sheets:
        if name != "Contracts":
            continue
        header = rows[0]
        for row in rows[1:]:
            d = dict(zip(header, row))
            lines.append(f"## Contract {d.get('Contract Number', '?')}")
            lines.append(f"VP: {d.get('Value', '?')}")
            lines.append(f"Protagen Marines target: {d.get('Protagen Marines', '?')}")
            lines.append(f"Ulfari target: {d.get('Ulfari', '?')}")
            lines.append(f"MDR Executive Unit target: {d.get('MDR Executive Unit', '?')}")
            lines.append(f"Custodia Silens target: {d.get('Custodia Silens', '?')}")
            lines.append("")
    out_c.write_text("\n".join(lines), encoding="utf-8")

    out_p = ROOT / "raw/the_warcode/protocol_cards_transcription.txt"
    lines = [
        "# Protocol Cards transcription — The Warcode Rulebook V.0.8.7-F",
        "",
        "**Source:** raw/the_warcode/spreadsheets/Warcode_Contract_Protocol_list.xlsx — Protocols sheet",
        "**Method:** via typed transcription (owner spreadsheet)",
        "**Confidence:** draft",
        "**Date:** 2026-08-25",
        "",
        "**Note:** Cross-check against protocol_cards.ocr.txt — Total Hunt rows in xlsx carry incorrect Magnet flavour (transcription error).",
        "",
    ]
    for name, rows in sheets:
        if name != "Protocols":
            continue
        header = rows[0]
        for row in rows[1:]:
            d = dict(zip(header, row))
            title = d.get("Protocol Title", "?")
            section = d.get("Map section", "?")
            lines.append(f'## Protocol "{title}" — {section}')
            lines.append(f"Flavour: {d.get('flavour_text', '')}")
            lines.append(f"Rule: {d.get('rule_text', '')}")
            lines.append("")
    out_p.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_c.name} and {out_p.name}")


if __name__ == "__main__":
    main()
