"""Hearthstone game state"""
from game.player import Player
from game.cards.deck import CardDeck


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self, cfg):
        self.player_A = Player('Pyjter', cfg)
        self.card_deck_A = CardDeck(self.player_A.name, cfg)

        self.player_B = Player('Mati', cfg)
        self.card_deck_B = CardDeck(self.player_B.name, cfg)

    def is_terminal_state(self):
        """Check if game is over (one player lost)"""
        is_player_A_dead = self.player_A.health == 0
        is_player_B_dead = self.player_B.health == 0
        return is_player_A_dead or is_player_B_dead

