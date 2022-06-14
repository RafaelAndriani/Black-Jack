import random


from Card import Card
from Player import Player


class Dealer(Player):
    def __init__(self):
        self.name = "Dealer Willgner"
        self.cards = []

    def give_cards(self, quant):
        cards = []
        for _ in range(quant):
            cards.append(Card.get_random_card())
        return cards
