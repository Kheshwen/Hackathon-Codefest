import json
from pathlib import Path
from app.models import Finding

_PATH = Path(__file__).parent.parent / "data" / "seed.json"
_DATA = json.loads(_PATH.read_text(encoding="utf-8"))
_INDEX = {e["value"]: e for e in _DATA["entries"]}

def lookup(extracted: dict) -> list[Finding]:
    findings = []
    for value in extracted["accounts"] + extracted["phones"]:
        entry = _INDEX.get(value)
        if entry:
            findings.append(Finding(
                check="mule_db",
                level="danger",
                reason=f"This {entry['type']} was reported {entry['reports']} times ({entry['note']}).",
            ))
    return findings