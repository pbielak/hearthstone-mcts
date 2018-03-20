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

    def __hash__(self):
        return hash((self.name, self.health, self.mana,
                     self.already_used_mana,
                     tuple(self.cards), tuple(self.minions)))

    def __eq__(self, other):
        if isinstance(other, BasePlayer):
            return hash(self) == hash(other)
            # return self.name == other.name and \
            #        self.health == other.health and \
            #        self.mana == other.mana and \
            #        self.already_used_mana == other.already_used_mana and \
            #        self.cards == other.cards and \
            #        self.minions == other.minions
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
