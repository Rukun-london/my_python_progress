numbers=[1,3,6,9,4,25,6,38,9,2]

#3rd method range in loop
largest=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
print(f"Largest number is : {largest}"
      )


print(largest)
#1st method
# largest=max(numbers)
# print(largest)

# 2nd method loop
# chosen=numbers[0]
# for num in numbers:
#     if num>chosen:
#         chosen=num
# print(chosen)




