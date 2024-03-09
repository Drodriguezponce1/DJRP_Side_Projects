from random import randint

start = randint(1,100)
print(start)
guesses = 0
i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))
li = []
while i != start:
    if i > 100 or i < 0:
        print("OUT OF BOUNDS!!")
        i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))
        continue

    li.append(i)
    if guesses == 0:
        if start - i <= 10:
            print("WARM!")
            i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))
        elif start - i > 10:
            print("COLD!")
            i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))
        guesses += 1    
        continue

    if abs(start - i) < abs(start - li[-2]):
        print("WARMER!")
        i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))
    else:
        print("COLDER!")
        i = int(input("PLEASE ENTER A NUMBER FROM 1 - 100: "))

    guesses += 1


print(f"Success!! It took you {guesses + 1} guesses!")