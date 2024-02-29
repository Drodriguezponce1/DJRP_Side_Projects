#using the .format() method
print("This is a string {}".format("INSERTED"))

print("WE ARE {0} {1} IN THE WORLD".format("CODING", "PYTHON"))
print("WE ARE {a} {b} IN THE WORLD".format(a = "CODING", b = "PYTHON"))
#can use numbers
print("Menu: Java Chip is ${}".format(13.99))

#formatting a float
result = 2342.345234234
print("The float was {a:1.4f}".format(a=result))

name = "Daniel"
age = 26
height = 5.10
print(f"His name is {name} and is {age} years old, and is {height:1.2f} height")