"""Card deck"""
from copy import deepcopy
import random

from game.cards.available_cards import get_all_available_cards


class CardDeck(object):
    """Represent one of the both available card decks, where players are
    pooling their cards from.

    Attributes:
        name (str): deck's owner (player name), mostly for debug reasons
        cards (list): list of card currently available in deck
    """
    def __init__(self):
        available_cards = get_all_available_cards()
        # There should be 2 cards of each type
        available_cards.extend(deepcopy(available_cards))
        self.cards = available_cards
        random.shuffle(self.cards)

        self.no_attempt_pop_when_empty = 0

    def is_empty(self):
        return not self.cards

    def pop(self):
        return self.cards.pop(0)

    def __repr__(self):
        fmt_str = "CardDeck: {cards}"

        return fmt_str.format(cards=self.cards)
