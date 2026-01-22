cal=int(input(" How many calculation: "))
n1=float(input("Enter a number,n1 : "))
n2=float(input("Enter a number,n2 : "))
count=1
while count  <= cal:
    print(f"calculation: {count}")

    
    operation=input("Enter an operation ( + - * / )  : ")
    if operation=="+":
        print(f"n1 + n2 = {(n1 + n2)}")
    elif operation== "-":
        print(f"n1 - n2 = {(n1 - n2)}")
    elif operation=="*":
        print(f"n1 * n2 = {(n1 * n2)}")
        
    elif operation=="/":
        if n2==0:
            print("valueError, zero can not be a divisor")
        else:
            print(f"n1 / n2 = {(n1 / n2)}")
    else:
        print(" invalid input.")
    count+=1