"""Player module"""
from game.cards.deck import CardDeck


class BasePlayer(object):
    """
    Health
    Mana points

    Deck
    Cards
    Minions
    """
    def __init__(self, name, cfg):
        self.name = name
        self.health = cfg.INITIAL_HEALTH
        self.mana = cfg.INITIAL_MANA
        self.already_used_mana = 0
        self.deck = CardDeck()
        self.cards = []
        self.minions = []
        self.cfg = cfg

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
        #                       max_health=self.cfg.INITIAL_HEALTH,
        #                       current_mana=self.already_used_mana,
        #                       max_mana=self.mana,
        #                       deck=self.deck,
        #                       cards=self.cards,
        #                       minions=self.minions)

        return self.name
