def sum(x,y):
    return x+y

def user_input():

    return int(input("Please enter a value: "))

if __name__ == "__main__":
    x = user_input()
    y = user_input()
    print(f"{x} + {y} = {sum(x,y)}")