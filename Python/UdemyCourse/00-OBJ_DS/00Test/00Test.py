#NUMBERS
# write an equation with *,/,exponent,+,- to get the value 100.25

goal = 100.25
x = ((10/2) *100)-400+(.5**2)
if goal == x:
    print("Success!")
    print("X: "+ str(x) )
else:
    print(f"Current value of X: {x}\nFailure, try again!")

# What is the value of the expression 4 * (6 + 5) 
    # 44
print(4* (6+5))

# What is the value of the expression 4 * 6 + 5 
    # 29
print(4*6+5)

# What is the value of the expression 4 + 6 * 5 
    # 34
print(4 + 6 * 5 )

# What is the type of the result of the expression 3 + 1.5 + 4?
    #float
print(type(3 + 1.5 + 4))

# What would you use to find a number’s square root, as well as its square?
    #square root: 
print(int(25**.5))
    #square: ** 2
print(5**2)

#STRINGS
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

s = 'hello'
# Print out 'e' using indexing
print(s[1])

# Reverse the string 'hello' using slicing:
s ='hello'
# Reverse the string using slicing
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
s ='hello'
# Print out the 'o'
# Method 1:
print(s[-1])
# Method 2:
print(s[4])

#LISTS
#Build this list [0,0,0] two separate ways.
# Method 1:
li = [0,0]
li.append(0)
print(li)
# Method 2:
li = [0,0]
lt = [0]
l = li + lt
print(l)

#Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'Goodbye'
print(list3)

#Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()
print(list4)

#DICTIONARY
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d["simple_key"])

d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

#TUPLES
# What is the major difference between tuples and lists?
    #a list is a mutable in order data structure while a tuple is a immudable data structure

# How do you create a tuple?
    # by either casting it into a tuple or defining it using ()
lis = [1,2,3]
t = tuple(lis)
tt = (1,2,3)

# Sets
# What is unique about a set?
    # sets save data in a distinct/unique way where duplicates are not allowed, and it saves the data where 
    # it is at, meaning that the values are not sorted
# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
#list5.sort()
s = set(list5)
print(s)

#BOOLEANS
# Answer before running cell
print(2 > 3) # False
# Answer before running cell
print(3 <= 2) # False
# Answer before running cell
print(3 == 2.0) # False
# Answer before running cell
print(3.0 == 3) # True
# Answer before running cell
print(4**0.5 != 2) # False

#Final Question: What is the boolean output of the cell block below?

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
print(l_one[2][0] >= l_two[2]['k1']) #False

#WE FINISHED THIS ASSESSMENT! GOT 100