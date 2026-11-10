"""
RECORD CHECK  -  my version
===========================

Name  :  Adam Khenchelaoui (M01120438)
Lane  :  IT
Date  :  10 November 2026

Run it:   python template.py

Each record is one server: hostname, GB used, GB total.
The records are loaded from servers.txt (in this LAB folder).
"""

from pathlib import Path

# The folder this file lives in, so servers.txt is found wherever you run it from
HERE = Path(__file__).parent


# ====================================================================== CLASS

class Record:
    """One server's disk usage: hostname, GB used and GB total."""

    over_limit_count = 0   # class-level: shared by every Record

    def __init__(self, label, value, limit):
        """Store the hostname, GB used and GB total on the new object."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return how much of the limit is used, as a percentage."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT (100%+), WARNING (90%+) or OK."""
        if self.percent() >= 100:
            return "OVER LIMIT"
        elif self.percent() >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue   # skip blank lines
            label, value, limit = line.split(",")
            records.append(Record(label.strip(), float(value), float(limit)))
    return records


records = load_records(HERE / "servers.txt")


# ==================================================================== OUTPUT

for record in records:
    status = record.status()   # call once, then reuse the variable

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  GB used     : {record.value:>10.1f}")
    print(f"  GB total    : {record.limit:>10.1f}")
    print(f"  Of limit    : {record.percent():>9.1f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

    if status == "OVER LIMIT":
        Record.over_limit_count += 1

print()
print(f"Checked {len(records)} servers. {Record.over_limit_count} were over limit.")


# ==========================================================================
# Before you finish:
#
#    [x] Run it and check every record's numbers by hand
#        (srv-01: 87 / 120 = 72.5%  ->  OK)
#    [x] Every method only reads/changes its OWN object (self)
#    [x] Every method and __init__ has a one-line docstring
#
# Independence check (r1 and r2 are separate objects):
#    r1 = Record("srv-01", 87, 120)
#    r2 = Record("srv-02", 130, 120)
#    r1.value = 50
#    print(r1.value, r2.value)    ->  50 130   (r2 did not change)
