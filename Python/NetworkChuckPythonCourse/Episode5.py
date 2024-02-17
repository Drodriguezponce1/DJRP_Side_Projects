# https://www.youtube.com/watch?v=Ec9WQGw4lW0&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=5
x = input("What is your name: ")
menu = {"BLACK COFFEE" : 3, "JAVA" : 4, "CAPPUCCINO": 8}

if(x == "Ben"):
    y = input("Hey "+ x +"! Are you evil: ")
    if(y == "No"):
        print("WELCOME " + x)
    else:
        print("BYEE!!!!")
        exit()
else:
    print("Hello " + x + ", thank you so much for coming in today!")

order = input("Menu: BLACK COFFEE, JAVA, CAPPUCINNO\nPlease enter which item you like: ")

t = True

while(t):
    if order in menu.keys():
        print("CHOSEN ITEM: " + order)

        amount = int(input("ENTER THE AMOUNT OF COFFEES YOU WANT: "))

        print("TOTAL AMOUNT: " + str(amount * menu[order]))
        t = False
    else:
        order = input("PLEASE ORDER SOMETHING ON THE MENU: ")