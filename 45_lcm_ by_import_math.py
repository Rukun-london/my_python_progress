import math
def lcm(a,b):
    if a==0 or b ==0:
        raise ValueError("LCM is not defined for zero.")
    bismillah=(a * b)//math.gcd(a,b)
    return bismillah
    
x=int(input("enter a number: "))
y=int(input("enter another number: "))
try:
    print (f"LCM of {x} and {y} is {lcm(x,y)} .")
except ValueError as e:
    print(e)
    