# iterable means to go through something

li = [1,2,3,4,5]

for values in li:
    print(f"Value: {values}\b")

# more examples

myList = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(myList)):
    if myList[i] % 2 == 0:
        print(f"{myList[i]} is even!")
    else:
        print(f"{myList[i]} is odd!")

# another example
s = 0
for values in myList:
    s += values

print(s)

#iterating a string

st = "Hello"

for letter in range(len(st)):
    print(st[letter])

y = "Please enter a even number: "
x = input(y)
while not (int(x) % 2 == 0):
    x = input(y)

print("You have passed the test!")

# tuple unpacking
myList = [(1,2),(3,4),(5,6),(7,8),(9,10)]

for values in myList:
    print(values)

# to unpack the tuples!!!!!

for a,b in myList:
    print(f"{a} and {b}")

# another example of unpacking by with more values

myList = [(1,2,3), (4,5,6), (7,8,9)]

for a,b,c in myList:
    print(f"{a} and {b} and {c}")

# iterate through a dictonary
d = {'k1':1, 'k2':2, 'k3':3}

for key,value in d.items():
    print(f"Key: {key}, Value: {value}")

x = input("Input a key: ")
if x in d.keys():
    print("Success!")