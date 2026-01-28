#time table genetator
x= int(input("enter a number for timetable: "))
print("+---------|-------+")
for i in range(1,12):
    print(f"| {i:>3} X {x} | {i*x :> 4}  |")
print("+---------|-------+")