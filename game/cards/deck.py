"""Card deck"""
import random

from game.cards.available_cards import get_all_available_cards


class CardDeck(object):
    """Represent one of the both available card decks, where players are
    pooling their cards from.

    Attributes:
        name (str): deck's owner (player name), mostly for debug reasons
        cards (list): list of card currently available in deck
    """
    def __init__(self, name):
        self.name = name
        self.cards = get_all_available_cards()
        random.shuffle(self.cards)

    def is_empty(self):
        return not self.cards

    def __repr__(self):
        fmt_str = "CardDeck: Name: {name}; " \
                  "Cards: {cards}"

        return fmt_str.format(name=self.name,
                              cards=self.cards)
