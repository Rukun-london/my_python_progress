count=int(input("how many shape do you want to check : "))

i=1
while i<=count:
    shape=input("For rectangle/square shape, press r or s :")
    if shape=="r":
        l=int(input(" enter the length of the shape in cm : "))
        w=int(input(" enter the width of the shape in cm : "))
        perimeter=2*(l+w)
        print(f" The perimeter of the rectangle is: {perimeter}")
    elif shape=="s":
        side=int(input(" enter the length of the shape in cm : "))
        perimeter=4*side
        print(f" The perimeter of the square is: {perimeter}")
    else:
        print(" Invalid input")
    i=i+1