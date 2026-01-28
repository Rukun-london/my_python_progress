def factorial_recurive(n):
    print(f"recursive {n}")
    if n<0:
        return None
    if n==0:
        return 1
    return n*factorial_recurive(n-1)
num=int(input("Enter a number : "))

print(f"factorial {num}! is {factorial_recurive(num)}")