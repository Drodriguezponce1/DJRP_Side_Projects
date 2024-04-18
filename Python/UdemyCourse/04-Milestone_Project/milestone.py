import random
board = [1,2,3,4,5,6,7,8,9]

def print_board(board):
    count = 0
    st = "|   "
    for x in range(0,len(board)):
      
       st += str(board[x])+"   |   "
       count += 1

       if count == 3:
           count = 0
           print(f"{st}\n=========================")
           st = "|   "

#print_board(board)

def player_input(player):

    choice1,choice2 = '',''
    display = f"Please select \'X\' or \'O\' for {player}: "

    choices = ['X','O']

    choice_flag = True
    while choice_flag:
        choice = input(display+"\n")
        choice = choice.upper()
        if choice in choices:
            choice1 = choice

            for values in choices:
                if choice1 != values:
                    choice2 = values
                    break
            
            choice_flag = False
        else:
            print("Wrong input! Please try again!")
    return choice1,choice2

#player_1,player_2 = player_input()
#print(f"{player_1}\t{player_2}")

def place_marker(board, marker,position):
    board[position - 1] = marker

#place_marker(board,"X", (8))
#place_marker(board,"X", (4))
#place_marker(board,"X", (0))
#print_board(board)

def win_check(board,marker):

    acrossTop = (board[0] == marker) and (board[1] == marker) and (board[2] == marker)
    acrossMid = (board[3] == marker) and (board[4] == marker) and (board[5] == marker)
    acrossBot = (board[6] == marker) and (board[7] == marker) and (board[8] == marker)
    downLeft = (board[0] == marker) and (board[3] == marker) and (board[6] == marker)
    downMid = (board[1] == marker) and (board[4] == marker) and (board[7] == marker)
    downRight = (board[2] == marker) and (board[5] == marker) and (board[8] == marker)
    diagnolLeft = (board[0] == marker) and (board[4] == marker) and (board[8] == marker)
    diagnolRight = (board[2] == marker) and (board[4] == marker) and (board[6] == marker)

    return acrossBot or acrossMid or acrossTop or downLeft or downMid or downRight or diagnolLeft or diagnolRight

#print(f"{win_check(board,'X')}")

def space_check(board,position):
    return board[position - 1] not in ['X','O']

#print(f"Is position {4} avaliable? {space_check(board,5)}")

def full_board_check(board):
    for values in board:
        if values in [1,2,3,4,5,6,7,8,9]:
            return False

    return True

#print(f"Is this board full: {full_board_check(board)}")

def available_positions(board):
    return [x for x in board if x not in ['X','O']]

def player_choice(board,marker):

    availablePositions = available_positions(board)
    
    display = f"Available positions: {availablePositions}\nPlease enter which position you want to put {marker}: "
    placement_flag = True
    while placement_flag and full_board_check(board) == False:
        choice = int(input(display))
        #print_board(board)

        if choice in availablePositions:
            placement_flag = False

            place_marker(board, marker, choice)
            
        else:
            print(f"Please enter a apporpriate position!!!")
        
def replay():

    repl = input("Would you like to play again? Y or N: ")

    return repl in ["Y",'y']

#print(replay())
 
def choose_first():
    return random.randint(0,1)

def grab_names():
    li = ['','']

    li[0] = input("Please enter the name of the first player: ")
    li[1] = input("Please enter the name of the first player: ")

    return li

print("Welcome to Tic Tac Toe!\n")
counter = 1
while True:

    print(f"Currently starting game: {counter}")
    players = grab_names()

    rando = choose_first()
    print("This person will go first: " + players[rando])

    dic = {}

    if rando == 1:
        dic[players[1]],dic[players[0]] = player_input(players[rando])
    else:
        dic[players[0]],dic[players[1]] = player_input(players[rando])

    turn = dic[players[rando]]

    game = True
    while game:
        if turn == 'X':
            print("Current Board: ")
            print_board(board)

            position = player_choice(board,'X')
           

            if (win_check(board, 'X')):
                for key,value in dic.items():
                    if value == 'X':
                        print_board(board)

                        print(f"Congrats {key} for the dub!")
                
                break
            else:
                if full_board_check(board):
                    print("Game ended in a draw!")
                else:
                    turn = 'O'
        elif turn == 'O':
            print("Current Board: ")
            print_board(board)

            position = player_choice(board,'O')
            #place_marker(board, 'O', position)

            if (win_check(board, 'O')):

                print_board(board)
                for key,value in dic.items():
                    if value == 'O':

                        print(f"Congrats {key} for the dub!")
                
                break
            else:
                if full_board_check(board):
                    print("Game ended in a draw!")
                else:
                    turn = 'X'
    if not replay():
        break
    else:
        counter += 1
        board = [1,2,3,4,5,6,7,8,9]
        game = True



print("Thanks for playing!")
    


