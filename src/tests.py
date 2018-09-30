from gof import *
import pytest

# test valid cards
card = Card('G1')
assert card.color == 'G'
assert card.value == '1'

# test invalid cards
with pytest.raises(ValueError):
    Card('P2')
with pytest.raises(ValueError):
    Card('GZ')
with pytest.raises(ValueError):
    Card('M2')
with pytest.raises(ValueError):
    Card('Y10')
with pytest.raises(ValueError):
    Card('YD')
with pytest.raises(ValueError):
    Card('RP')
    
# test generate deck of cards
deck = Deck()
assert all(isinstance(card, Card) for card in deck)
assert len(deck) == 3*10*2 + 4

# test player bad init
with pytest.raises(TypeError):
    Player()
with pytest.raises(ValueError):
    Player([])
with pytest.raises(ValueError):
    Player([Card('R1')])
with pytest.raises(ValueError):
    Player([Card('R1'), Card('R2')])
with pytest.raises(ValueError):
    Player(NORMAL_CARDS[:16])

# test player init
hand = [Card(card) for card in NORMAL_CARDS[:16]]
player = Player(hand)
assert len(player.hand) == 16

# test game init
game = Game(players=3)
assert len(game.players) == 3
for player in game.players:
    assert isinstance(player, Player)
    assert len(player.hand) == 16

print('Passed!')