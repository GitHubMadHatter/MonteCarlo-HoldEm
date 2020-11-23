import random

class Card:
    def __init__(self, suit, index):
        self.suit = suit
        self.index = index
        
    def getDisplayFile(self):
        return self.index + self.suit + ".png"

class Deck:
    def __init__(self):
        self.cards = []
        numbers = [i for i in range(1,14)]
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        for suit in suits:
            for num in numbers:
                new_card = Card(suit, num)
                self.cards.append(new_card)
        random.shuffle(self.cards)    

    def getCard(self):
        card = self.cards[0]
        self.cards.remove(card).append(card)
        return card

class Player:
    def __init__(self, balance):
        self.balance = balance
        self.hand = []
        
    def updateBalance(self, balance):
        self.balance += balance
        if self.balance <= 0:
            return False
        return True

    def addToHand(self, deck):
        self.hand.append(deck.getCard())
        
class Game:
    pass
    
