def factorial(n):
    if n==0:
        return 1
    else:
        facto=1
        for i in range (1, n+1):
            facto=facto*i
        return facto

num=int(input("Enter a number for factorial : "))           
print(f"Factorial {num} is {factorial(num)}")