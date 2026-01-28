n1,n2=0,1
nth_term=int(input("enter the nth_term: "))
count=0
fibonacci=[]
while count<nth_term:
    fibonacci.append(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1
print(f"fibonacci:{fibonacci}")