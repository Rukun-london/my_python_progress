#Genarate a random number
import random
print(f"Random number is : {random.randint(1,100)}")
print(random.random())
print(f" pick a random decimal in range: {random.uniform(3.2 , 7)}")
print(f"Pick a random element:  {random.choice(["Rukun","Parveen", "Hidayah", "Fawzan"])}")
print(f"Pick a random element:  {random.choice(["Ele","Goat", "cat", "dog"])}")
print(f"Pick a random element:  {random.choice(["good","bad", "cute", "moster"])}")
print(f"Return:  { random.choices([32,80,5,9,8,100,12,6],k=4) }  ")
nums=[32,80,5,9,8,100,12,6]
random.shuffle(nums)
print(nums)
