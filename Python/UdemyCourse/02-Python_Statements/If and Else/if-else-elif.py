#control flow using if, else, and elif
# this is essentially just like Java
    #java uses if, else, else if

if (1 == 2):
    print("Success!")
else:
    print("Failure!")

if True:
    print("Hello!")

# random example 1
hungry = input("Are you hungry? ")

if (hungry == "yes"):
    print("YOU ARE HUNGRY!")
else:
    print("YOU ARE NOT HUNGRY!")

# random example 2
m = {1:2}
n = [1,2,3,4,5,6,7]
if 1 in n:
    print(m[1])