"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
     
hostname = input("Enter hostname: ")
gb_used = float(input("Enter GB used: "))     
gb_total = float(input("Enter total GB: "))

# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = gb_total - gb_used  # 
percent = (gb_used / gb_total * 100)     # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"
if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"
   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"{'GB used':>12}:{gb_used:>10.2f}")
print(f"{'GB total':>12}:{gb_total:>10.2f}")
print(f"{'Difference':>12}:{difference:>10.2f}")
print(f"{'Percent':>12}:{percent:>10.2f}%")
print(f"{'status':>12}:{status}")

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
