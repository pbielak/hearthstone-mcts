"""Player module"""


class BasePlayer(object):
    """
    Health
    Mana points

    Deck
    Cards
    Minions
    """

    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        self.name = name
        self.health = health
        self.mana = mana
        self.already_used_mana = already_used_mana
        self.deck = deck
        self.cards = cards
        self.minions = minions

    def play_turn(self, game_state):
        pass

    def is_dead(self):
        return self.health <= 0

    def __repr__(self):
        return "Player: {}".format(self.name)
