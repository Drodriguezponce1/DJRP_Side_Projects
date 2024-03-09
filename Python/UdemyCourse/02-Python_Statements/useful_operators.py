# range

myList = [1,2,3]

for num in range(10): # can also have a starting point range(4,10)
    print(num)

l = list(range(4,10)) # [4,10)

print(l)

# enumurate
index = 0
word = "abcde"

for letter in word:
    print(word[index])
    index +=1

# using enum

for item in enumerate(word):
    print(item)

for index, letter in enumerate(word):
    print(f"{index} and {letter}")

li1 = [1,2,3]
li2 = ['a','b','c']

for item in zip(li1, li2):
    print(item)

# random one with 3 lists
li3 = [1,2,3]

for a,b,c in zip(li1,li2,li3):
    print(f"{a} and {b} and {c}")

li = list(zip(li1, li2, li3))
print(li)

# using the 'in' operator to check whether something is in something
if "hello" in "helloorld":
    print("Success!")

# min and max function
myList = [10,20,30,40,50]

print(max(myList))
print(min(myList))

#method from the random library
from random import shuffle
myList = [1,2,3,4,5,6,7,8,9]
shuffle(myList)
print(myList)
