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
        # fmt_str = "Player: {name}; Health: {current_health}/{max_health}; " \
        #           "Mana: {current_mana}/{max_mana}; " \
        #           "Deck: {deck}; " \
        #           "Cards: {cards}; " \
        #           "Minions: {minions}"
        #
        # return fmt_str.format(name=self.name,
        #                       current_health=self.health,
        #                       max_health=config.INITIAL_HEALTH,
        #                       current_mana=self.already_used_mana,
        #                       max_mana=self.mana,
        #                       deck=self.deck,
        #                       cards=self.cards,
        #                       minions=self.minions)

        return self.name
