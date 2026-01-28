import time
import sys

start = int(input("Enter a start range: "))
end = int(input("Enter an end range: "))

armstrong_numbers = []
total_numbers = end - start

for i, num in enumerate(range(start, end), start=1):
    # Progress bar
    progress = int((i / total_numbers) * 30)
    bar = "#" * progress + "-" * (30 - progress)
    sys.stdout.write(f"\r[{bar}] {i}/{total_numbers} Checking {num}")
    sys.stdout.flush()
    time.sleep(0.05)

    power = len(str(num))
    total = sum(int(digit)**power for digit in str(num))

    if num == total:
        armstrong_numbers.append(num)

print("\nArmstrong numbers:", armstrong_numbers)
