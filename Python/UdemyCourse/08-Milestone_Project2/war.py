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
for i,cards in enumerate(new_deck.all_cards):
    print(f"Card {i}: {cards}")

card = new_deck.deal_one()

for i,cards in enumerate(new_deck.all_cards):
    print(f"Card {i}: {cards}")

print(card)