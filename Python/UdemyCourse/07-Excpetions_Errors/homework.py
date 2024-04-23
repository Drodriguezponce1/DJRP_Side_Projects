print("====================== PROBLEM 1 ======================")
try:
    counter = 0
    for i in [1,'b','c']:
        print(i**2)
        counter+=1
except TypeError:
    print("Came accross a TypeError!")
finally:
    print(f"Could only calculate {counter} square roots")

print("====================== PROBLEM 2 ======================")

try:
    x = 5
    y = 0

    z = x/y
    flag = True
except ZeroDivisionError:
    print("Came accross a Zero Division Error, meaning that you are trying to divide by zero!")
    flag = False
finally:
    if flag:
        print("Division was a success!")
    else:
        print("Could not compute!")


print("====================== PROBLEM 3 ======================")

def ask():
    while True:
        try:
            result = int(input("Input an integer: "))
            print(f"Thanks, your number squared is: {result**2}")
        except:
            print("An error has occured! Please try again!")
            flag = False
        else:
            break

ask()

