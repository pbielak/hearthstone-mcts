"""Player module"""
from game import config
from game.cards import deck


class BasePlayer(object):
    """
    Health
    Mana points

    Deck
    Cards
    Minions
    """
    def __init__(self, name):
        self.name = name
        self.health = config.INITIAL_HEALTH
        self.mana = config.INITIAL_MANA
        self.already_used_mana = 0
        self.deck = deck.CardDeck()
        self.cards = []
        self.minions = []

    def play_turn(self, game_state):
        pass

    def is_dead(self):
        return self.health <= 0

    def __repr__(self):
        return "Player: {}".format(self.name)
