#tuples cant be changed
t = (1,2,3)
l = [1,2,3]

print(type(t))
print(type(l))

#count hoe many x appear in a tuple
print(t.count(1))

#grab the index of x
t = ('a','b','c')
print(t.index("a"))

#cannot reassign a tuple!
print(t[2])
# cant do this: t[2] = "c"

t = (1,2,3)
print(t)
li = []
for values in t:
    li.append(values)

li[1] = 7

t = tuple(li)

print(t)


