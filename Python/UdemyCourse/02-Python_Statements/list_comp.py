st = 'hello'
#make a list out of the string

myList = [letter for letter in st]

print(myList)

# another example
x = [y for y in "asdfasdfasdfa"]

x = [g**2 for g in range(1,11)]

print(x)

li = [x for x in range(1,21) if x %2 == 0]
print(li)

# example to convert a list of celsius to fer
celsius =  [ 0, 30,31.2,33,50]

f = [ ((9/5)*x + 32)for x in celsius]

for cel, fer in zip(celsius, f):
    print(f"{cel}c = {fer}f")

# more....
results = [x if x %2 == 0 else 'ODD' for x in range(1,11)]
print(results)

#nested loop 
myList = []

for x in [1,2,30]:
    for y in [1,2,4]:
        myList.append(x*y)

print(myList)

# nested list comp
myList = [x*y for x in [1,2,30] for y in [1,2,4]]
print(myList)