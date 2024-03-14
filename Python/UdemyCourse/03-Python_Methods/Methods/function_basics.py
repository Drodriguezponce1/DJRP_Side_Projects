def say_hello():
    return f"Hello World"

print(say_hello())

def say_hello(name):
    print(f"Hello {name}")

say_hello("Jeff")

# if a method was used but no paramter was given
def sum(one, two = 3):
    print(f"{one} + {two} = {one+two}")

sum(1)
sum(1,6)

#how to make it where you can only input x and y
