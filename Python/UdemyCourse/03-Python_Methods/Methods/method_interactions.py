from random import shuffle
#random list module
example = [1,2,3,4,5]
shuffle(example)

print(example)

def shuffle_list(li):
    shuffle(li)
    return li

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Please select 0, 1, or 2: ")

    return int(guess)    

def check_guess(li,guess):
    if li[guess] == 'O':
        print("Guess was correct!")
    else:
        print("Guess is Wrong!")

def game():
    li = ['','O','']
    shuffled = shuffle_list(li)
    guess = player_guess()
    check_guess(shuffled, guess)
    print(shuffled)

game()
