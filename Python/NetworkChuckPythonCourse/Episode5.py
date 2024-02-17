x = input("What is your name: ")


if(x == "Ben"):
    y = input("Hey Ben! Are you evil: ")
    if(y == "No"):
        print("WELCOME " + x)
    else:
        print("BYEE!!!!")
        exit()
else:
    print("Hello " + x + ", thank you so much for coming in today!")