n=int(input("enter a number for factorial: "))
if n<0:
    print("factorial does not exit for negative number.")
elif n==0:
    print("factorial 0 is 1.")
else:
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    print(f"factorial {n} = {factorial}")