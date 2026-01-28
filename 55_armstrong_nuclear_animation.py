#Armstrong number nuclear

def armstrong_number(start,end):
    return [
            num for num in range(start,end) 
            if num==sum(int(digit)**len(str(num)) for digit in str(num))    ]
start=int(input("Enter a start range : "))
end=int(input("Enter a end range : "))
print(f"\nArmstrong numbers: {armstrong_number(start,end)}")