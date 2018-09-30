from itertools import product
from random import shuffle

COLORS = 'GYR'
NUMBERS = '123456789T'
NORMAL_CARDS = 2 * list(product(COLORS, NUMBERS))
SPECIAL_CARDS = ['M1', 'GP', 'YP', 'RD']
VALID_CARDS = NORMAL_CARDS + SPECIAL_CARDS

class Card:
    def __init__(self, spec):
        color, value = spec
        if (color, value) not in VALID_CARDS:
            raise ValueError('Invalid card')
        self.color, self.value = spec


class Deck:
    def __init__(self):
        self.cards = []
        for color, value in NORMAL_CARDS:
            spec = color + value
            card = Card(spec)
            self.cards.append(card)
        for color, value in SPECIAL_CARDS:
            spec = color + value
            card = Card(spec)
            self.cards.append(card)
        shuffle(self.cards)
        
    def __iter__(self):
        return iter(self.cards)
        
    def __len__(self):
        return len(self.cards)
        
    def deal(self, n):
        return [self.cards.pop() for i in range(n)]
        
class Player:
    def __init__(self, hand):
        if len(hand) != 16:
            raise ValueError('Player needs 16 cards')
        if not all(isinstance(card, Card) for card in hand):
            raise ValueError('Hand must comprise Card objects')
        self.hand = hand
        
class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.players = [Player(self.deck.deal(16)) for p in range(players)]