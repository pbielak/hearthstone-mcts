"""Card deck"""


class CardDeck(object):
    """Represent one of the both available card decks, where players are
    pooling their cards from.

    Attributes:
        name (str): deck's owner (player name), mostly for debug reasons
        cards (list): list of card currently available in deck
    """
    def __init__(self, name, cfg):
        self.name = name
        self.cards = []
        # cfg should be used to generate initial list of cards in deck(!)
