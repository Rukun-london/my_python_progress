#the quadratic equation is 
# ax**2+bx+c=0
#x=(-b+-(b**2-4ac)**.5)/2a


#case2
import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
D=(b**2-4*a*c)
print(f"discriminant={D}")
if D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print(f"Real root x1= {root1}")
    print(f"Real root x2= {root2}")
elif D==0:
    root=-b/(2*a)
    print(f"Real repeated root x= {root}")
else:
    real_part=-b/(2*a)
    ima_part=(math.sqrt(-D)/(2*a))*1j
    x1=real_part+ima_part
    x2=real_part-ima_part
    print(f"complex root x1= {x1}")
    print(f"complex root x2= {x2}")
