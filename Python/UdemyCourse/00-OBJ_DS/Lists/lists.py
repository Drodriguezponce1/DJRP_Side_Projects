#starting with lists
my_list = [1,2,3]

#get the length of the list
x = len(my_list)

#grabbing an index just like in java
z = my_list[0]

#splicing!
y = my_list[:2]
print(y)

#adding lists!
start = [1,2,3]
end = [4,5,6]
total = start + end
print(f"Starting list: {start}\nEnding list: {end}\nAdding both lists: {total}\nSplicing the total list: {total[2:5]}")

#changing elements in a list
li = [1,2,3,4]
li[0] = 999
print(li)

#add elements to a list
li.append(5)
print(li)

#add an element using insert()
li.insert(2,8)
print(li)

#remove the last element
popped = li.pop()
print(str(popped))
print(li)

#remove at a specific index
popped = li.pop(2)
print(str(popped))
print(li)

#sorting a list
li = [1,5,2,11,7]
li.sort()
print(li)

#reverse a list
li = [1,5,2,11,7] 
li.reverse()
print(li)

#just practicing and testing
st = "Hello World"
li = list(st)
print(li)
li.sort()
print(li)
li.remove(" ")
print(li)