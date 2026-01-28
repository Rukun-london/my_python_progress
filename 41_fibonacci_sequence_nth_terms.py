nth_term=int(input("enter the nth term: "))
n1,n2=0,1
count=0
if nth_term==0:
    print("Enter a positive integer.")
else:
    while count < nth_term:
        print(f"{n1}")
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1