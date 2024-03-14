# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.

def myfunc(x,y,z):
    if z == True:
        return x
    
    return y

print(myfunc("Hello","Goodbye", False))