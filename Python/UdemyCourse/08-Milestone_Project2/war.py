import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank.capitalize()]
    

    def __str__(self):
        return f"[Rank: {self.rank}, Suit: {self.suit}]"

'''
two_hearts = Card("Hearts", "two")
three_hearts = Card("Clubs", "Three")
print(two_hearts)
print(two_hearts.value)

print(three_hearts.value > two_hearts.value)'''

class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create a Card object
                card = Card(suit, rank)
                self.all_cards.append(card)
    
    def shuffle(self):
       random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

new_deck = Deck()

new_deck.shuffle()
'''for i,cards in enumerate(new_deck.all_cards):
    print(f"Card {i}: {cards}")

card = new_deck.deal_one()

for i,cards in enumerate(new_deck.all_cards):
    print(f"Card {i}: {cards}")

print(card)'''

class Player():

    def __init__(self,name):
        self.name = name
        self.cards = []
    
    def remove_one(self):
        return self.cards.pop(0)

    def add_cards(self,cards):
        if type(cards) == type([]):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.cards)} cards!"

'''
player = Player("Daniel")
print(player)

player.add_cards(new_deck.all_cards[0])
print(player)

player.add_cards([new_deck.all_cards[0],new_deck.all_cards[0],new_deck.all_cards[0]])
print(player)

player.remove_one()
print(player)'''

#Game setup
player_one = Player("One")
player_two = Player("Two")

deck = Deck()
deck.shuffle()

for cards in range(26):
    player_one.add_cards(deck.deal_one())
    player_two.add_cards(deck.deal_one())

print(player_one)
print(player_two)

game_on = True

round = 0
#while game_on

while game_on:

    round += 1
    print(f"Starting round {round}!")

    if len(player_one.cards) == 0:
        print(f"Player One, has ran out of cards! Player Two wins!")
        game_on = False
        break
    elif len(player_two.cards) == 0:
        print(f"Player Two, has ran out of cards! Player One wins!")
        game_on = False
        break
    
    #Start a new round
    #The cards that are in play!
    player_one_cards = []
    player_two_cards = []

    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())
   
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print("War!")

            if len(player_one.cards) < 3:
                print("Player one unable to declare war!")
                print("Player two wins! ")
                game_on = False
                break
            elif len(player_two.cards) < 3:
                print("Player two unable to declare war!")
                print("Player one wins! ")
                game_on = False
                break
            else:
                for x in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

