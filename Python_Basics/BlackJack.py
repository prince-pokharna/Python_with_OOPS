import random

suits = ["spades" , "diamond", "clubs","heart"]
rank = ["A", 2,3,4,5,6,7,8,9,10, "J", "Q", "K"]

class Card :
    def __init__(self, suit,rank):
        self.rank = rank
        self.suit = suit

    def __str__():
        return f"{self.rank} of {self.suit}"


class Deck :
    def __init__(self):
        self.cards = []
        for suit in suit:
            for rank in ranks:
                self.cards.append(Card(suits,rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    def deal(self, number):
        
        dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                dealt.append(self.cards.pop())
        return dealt
    