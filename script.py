#comments 1
# str
# int
# float
# bool
# bytes
# tuple
from unittest.util import sorted_list_difference

name: str="Georgia Stanway"

age=20
aggregate:float = 77.9
is_raining:bool = False

x: tuple = (1,2,3)
list_names: list =["John", "Mary"]
nums:list = [2,3,4,1,43,123,321,1]

data: dict = {'name':"Bob", 'age': 20 }

print(data)


print(nums)



def get_Largest(numbers , n):
    numbers.sort()

    return numbers[-n:]

sorted_list = get_Largest(nums, 5)
# print(sorted_list)

# List comprehension

fruits=["banana","apple","cherry","kiwi"]

for i in fruits:
    print(i)

    if i == "kiwi":
        break

for j in range(2,30,3):# 2 to 30 every 3 numbers, excluding 30
    print(j)

i=9

while i<7:
    print(i)
    i += 1

else:
    print ("i is no longer less than 7")