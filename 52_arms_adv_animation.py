import time
import sys

start = int(input("Enter a start range: "))
end = int(input("Enter an end range: "))

armstrong_numbers = []

for num in range(start, end):
    print(f"\nChecking {num}...")
    time.sleep(0.1)

    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        calc = int(d)**power
        total += calc
        print(f"  {d}^{power} = {calc}")
        time.sleep(0.1)

    print(f"  Total = {total}")
    time.sleep(0.1)

    if num == total:
        print("  → Armstrong number found!")
        armstrong_numbers.append(num)
    else:
        print("  → Nope!")

print("\nAll Armstrong numbers:", armstrong_numbers)
