# infinite into its not true/false

# while 1==1:
#     print("Infinite Loop!")

x = 1

while x <= 10:
    print(f"{x} x {2} = {x *2}")
    x +=1
else:
    print("X has reached its limit of 10!")

# breaK = break out of the current loop
l = "Fanny"

for letter in l:
    if letter == 'a':
        break
    print(letter)

# continue = break but it continues 
l = "Danny"

for letter in l:
    if letter == 'a':
        continue
    print(letter)

# example

x = 0

while x < 10:
    if x % 2 == 0:
        x += 1
        continue
    print(x)
    x += 1
