year=int(input("enter a year: "))
if year % 400==0:
    print(f"{year} is a leap year.")
elif year % 100==0: 
    print(f"{year} is a not leap year.")
elif year % 4==0:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is a not 202leap year.")
    
            or
            
for i in range(10):
    year=int(input("enter a year: "))
    if year % 400==0 or year % 4 ==0 and year % 100!=0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is a not a leap year.")
        
            or
            
for i in range(10):
    year=int(input("enter a year: "))
    if year % 400==0:
        print(f"{year} is a leap year.")
    elif year % 4 ==0 and year % 100!=0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
        
            or
for i in range(10):
    year=int(input("enter a year: "))
    if year % 400==0:
        print("{0} is a leap year".format(year))
    elif year % 4 ==0 and year % 100!=0:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
