
#lowest common multiple 
def lcm(a,b):
    if a==0 or b ==0:
        raise ValueError("LCM is not defined for zero.")
    #if a == b:
       # return a
    greater=max(a,b)
    while True:
        if greater % a ==0 and greater % b== 0:
            return greater
        greater+=1
    
x=int(input("enter a number: "))
y=int(input("enter another number: "))
try:
    print (f"LCM of {x} and {y} is {lcm(x,y)} .")
except ValueError as e:
    print(e)
    