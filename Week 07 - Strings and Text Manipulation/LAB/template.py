"""
RECORD CHECK  -  my version
===========================

Name  :  Adam Khenchelaoui (M01120438)
Lane  :  IT
Date  :  10 November 2026

Run it:   python template.py

Each raw line is one server reading, e.g. "  Srv-01 , used=87 , total=100  ".
The raw lines are loaded from raw_servers.txt (in this LAB folder).
"""

from pathlib import Path

# The folder this file lives in, so the file is found wherever you run it from
HERE = Path(__file__).parent


# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Clean one messy raw line and return it as a dict with converted values."""
    line = raw_line.strip().lower()
    hostname_part, rest = line.split(",", 1)

    record = {"hostname": hostname_part.strip()}
    for piece in rest.split(","):
        key, value = piece.split("=")
        record[key.strip()] = float(value.strip())

    return record


def status_of(used, total):
    """Return OVER LIMIT (100%+), WARNING (90%+) or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# ====================================================================== INPUT

raw_records = []
with open(HERE / "raw_servers.txt") as file:
    for line in file:
        if line.strip():          # skip blank lines
            raw_records.append(line)


# =============================================================== PROCESS + OUTPUT

flagged = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["used"], record["total"])
    print(record, "->", status)

    if status != "OK":
        flagged += 1

print()
print(f"Checked {len(raw_records)} records. {flagged} were flagged.")


# ==========================================================================
# Before you finish:
#
#    [x] Run it against at least 5 genuinely messy raw records (see raw_servers.txt)
#    [x] Checked one by hand: "  Srv-01 , used=87 , total=100  "
#        -> {'hostname': 'srv-01', 'used': 87.0, 'total': 100.0} -> OK
#    [ ] Run it with a value that will not convert to a number, e.g. used=abc
#        Error: ValueError: could not convert string to float: 'abc'
#    [x] Every function does one job, with a docstring
