#This vid involved Math!
#https://www.youtube.com/watch?v=T6OLDHAWjjA
x = input("Name: ")
y = input("Menu: BLACK COFFEE, MATCHA, JAVA\nPlease enter which item you like: ")
z = int(input("How many would you like? "))
amount = 0
if(y == "BLACK COFFEE"):
    amount = 3.66
elif(y == "MATCHA"):
    amount = 4.99
else:
    amount = 78.33

print("Thank you for ordering " + x + "! Your order of " + y + " will be available shortly! ")
print("Total Price: " + str(amount * z))
