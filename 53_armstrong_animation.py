
import time
import sys

start=int(input("Enter a start range : "))
end=int(input("Enter a end range : "))
armstrong_number=[]

spinner = ["|", "/", "-", "\\"] 
for num in range(start, end):
    for s in spinner:
        sys.stdout.write(f"\rChecking {num} ........{s} ")
        sys.stdout.flush()
        time.sleep(.05)
    power=len(str(num))
    total=sum(int(digit)**power for digit in str(num))
    if num==total:
        armstrong_number.append(num)
print(f"\nArmstrong numbers: {armstrong_number}")