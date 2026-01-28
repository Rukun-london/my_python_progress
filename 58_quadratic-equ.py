import cmath
def quadratic(a,b,c):
    discriminant=b**2-4*a*c
    root1= (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2=(-b-cmath.sqrt(discriminant))/(2*a)
    return root1,root2
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=float(input("Enter the third number: "))
r1,r2=quadratic(a,b,c)
print(f"The roots are: {r1} and {r2}")
