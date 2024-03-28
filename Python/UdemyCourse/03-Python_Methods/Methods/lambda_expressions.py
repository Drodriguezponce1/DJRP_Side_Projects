#using the built in map

def sqr(x):
    return x**2

nums = [1,2,3,4,5]

for item in map(sqr,nums):
    print(item)

#or
    
li = list(map(sqr,nums))
print(li)

#another example
def splicer(str):
    if len(str) % 2 == 0:
        return "EVEN"
    
    return str[0]

names = ['Andy', 'Eve','Sally']

print(list(map(splicer,names)))

#using the filter method
def check_even(x):
    return x%2 == 0

nums = [1,2,3,4,5,6]
print(list(filter(check_even,nums)))

#lambda
def square(x): return x ** 2

square = lambda num: num ** 2

li = list(map(lambda num: num ** 2, nums))
print(li)

#grab first letters of a list of strings
names = ['Andy', 'Eve','Sally']

first = list(map(lambda str:str[0],names))
print(first)
