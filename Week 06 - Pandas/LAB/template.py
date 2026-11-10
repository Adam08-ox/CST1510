"""
RECORD CHECK  -  my version
===========================

Name  :  Adam Khenchelaoui (M01120438)
Lane  :  IT
Date  :  10 November 2026

Run it:   python template.py

Each row is one server: hostname, GB used, GB total.
The data is read from servers.csv (in this LAB folder).
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# The folder this file lives in, so the files are found wherever you run it from
HERE = Path(__file__).parent


# ==================================================================== LOAD

df = pd.read_csv(HERE / "servers.csv")


# ================================================================= PROCESS

df["percent"] = ((df["used_gb"] / df["total_gb"]) * 100).round(1)

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)


# ================================================================== OUTPUT

print("All servers:")
print(df)

# Only the rows that are not OK - a boolean filter, no loop
print("\nNeeds attention:")
print(df[df["status"] != "OK"])

# Count per status group
print("\nServers per status:")
print(df.groupby("status")["hostname"].count())

# Save the full DataFrame to a new CSV
df.to_csv(HERE / "servers_report.csv", index=False)
print("\nSaved servers_report.csv")

# One bar chart of the counts per status, saved as a PNG
df["status"].value_counts().plot(kind="bar")
plt.title("Servers per status")
plt.xlabel("Status")
plt.ylabel("Number of servers")
plt.tight_layout()
plt.savefig(HERE / "servers_status_chart.png")
print("Saved servers_status_chart.png")


# ==========================================================================
# Before you finish:
#    [x] Checked by hand for one row: srv-01, 87 / 120 = 72.5%  ->  OK
#    [x] Only one condition is used, so no & / | needed
#    [x] Column names match the CSV header exactly: hostname,used_gb,total_gb
