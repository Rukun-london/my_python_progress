
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
discriminant=(b**2-4*a*c)
r1=(-b+discriminant**(1/2))/(2*a)
r2=(-b-discriminant**(1/2))/(2*a)
print(f"The roots are: {r1} and {r2}")
