# https://www.youtube.com/watch?v=Ec9WQGw4lW0&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=5
x = input("What is your name: ")
menu = "BLACK COFFEE, ESPRESSO, LATTE, CAPPUCINO, FRAPPUCINO"

if(x == "Ben"):
    y = input("Hey Ben! Are you evil: ")
    if(y == "No"):
        print("WELCOME " + x)
    else:
        print("BYEE!!!!")
        exit()
else:
    print("Hello " + x + ", thank you so much for coming in today!")