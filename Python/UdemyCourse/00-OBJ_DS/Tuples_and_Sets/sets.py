#can only have distinct values in a set

my_set = set()
my_set.add("1")
my_set.add(2)
print(my_set)

my_set.add(2)
print(my_set)

#can easily get rid of duplicates
li = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5]
s = set(li)
print(s)

#what if its an unsorted list
li = [3,5,2,6,1,4,5,6,2,1,3,5,2,3,1]
s = set(li)
print(s)

# can even set a string
st = "MISSISSIPpI"
s = set(st)
print(s)