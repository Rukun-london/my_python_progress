n=int(input("enter a range: "))
print("The prime numbers are: ")
for num in range(n+1):
    if num>1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            print(num)
            
            or
            
n=int(input("enter a range: "))
prime=[]
for num in range(n+1):
    if num>1:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            prime.append(num)
print(f"The prime number in a range of {n} are: {prime}")

        or
        
n = int(input("Enter a range: "))

sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(n**0.5) + 1):
    if sieve[i]:
        for j in range(i*i, n+1, i):
            sieve[j] = False

primes = [i for i in range(n+1) if sieve[i]]
print(primes)


            or
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a range: "))
primes = [num for num in range(n+1) if is_prime(num)]
print(primes)


                or
                
n = int(input("Enter a range: "))

primes = [
    num for num in range(2, n+1)
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1))
]

print(primes)


            or 
            
n = int(input("Enter a range: "))

sieve = [True] * (n+1)
for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        sieve[i*i : n+1 : i] = [False] * len(range(i*i, n+1, i))

primes = [i for i in range(2, n+1) if sieve[i]]
print(primes)
  
  
                or  
                
                
def primes_up_to(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

n = int(input("Enter a range: "))
print(list(primes_up_to(n)))
