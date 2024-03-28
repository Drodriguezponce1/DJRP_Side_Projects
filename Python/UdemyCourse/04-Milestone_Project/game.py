#grid
def grid(row1, row2, row3):
    print(f"{row1}\n{row2}\n{row3}")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
grid(row1,row2,row3)

#user input
user = int(input("Choose an index position: "))

print(type(user))

def user_choice():

    ran = False
    while ran == False:

        choice = input("Please enter a number between (0 - 10): ")


        if not choice.isdigit():
            print("Please input a integer value!!!!")
            continue
        else:
            choice = int(choice)

        if choice not in range(0,11):
            print("You are out of range! Try again! ")
        else: 
            ran = True
    
    return choice

choice = user_choice()

