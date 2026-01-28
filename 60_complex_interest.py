#complex interest
def total_amount_with_interest(principal,interest_rate):
    year = 1
    while year <= time:
        total_amount_with_interest = principal * (1 + interest_rate / 100)
        year += 1
    return

principal=int(input("Enter the Principal amount:"))
interest_rate=float(input("Enter the Interest rate:"))
time=int(input("How many years:"))


print(f"If you borrow £{principal} total money you need to pay back £{total_amount_with_interest()} after {time} years.")
