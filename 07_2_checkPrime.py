#a python program to check a prime number
num=int(input("enter a number: "))
if num <=1:
    print(f"{num} is not a prime number.")
else:
    for i in range(2, int(num**.5+1)):
        if num % i ==0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")