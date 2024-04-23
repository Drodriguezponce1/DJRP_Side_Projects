def add(x,y):
    return x + y

print(add(1,2))

# we need to be careful to not send a string!

try:
    result = 10 + 50

except:
    print("Looks like you are not adding correctly!")
else:
    print("Adding was a success!")
finally:
    print("Hello")


try:
    f = open('testfile','r')
    f.write("Write a test line!")
except TypeError:
    print(TypeError.__str__)
    print("There was a TypeError")
except  OSError:
    print(str(OSError))
finally:
    f.close()
    print("I always run!")


def ask_for_int():

    while True:
        try:
            result = int(input("Please provide an input: "))
        except:
            print("That is not a integer!!")
            continue
        else:
            return result
        finally:
            print("EOM\n")

r = ask_for_int()
print(r)