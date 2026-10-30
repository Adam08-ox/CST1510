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

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.
def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    print()
    print("=" * 40)
    print(f" RECORD CHECK - {label:>10.2f}")
    print("=" * 40)
    print(f"{'Used':<12}: {value:>10.2f}")
    print(f"{'Total':<12}: {limit:>10.2f}")
    print(f"{'Free':<12}: {difference:>10.2f}")
    print(f"{'Percent':<12}: {percent:>9.2f} %")
    print(f"{'Status':<12}: {status:>10}")
    print("=" * 40)
over_limit_count = 0

while True:
    label = input("\nEnter hostname (or 'quit' to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter GB used: "))
    limit = float(input("Enter GB total: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"Records OVER LIMIT: {over_limit_count}")

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
