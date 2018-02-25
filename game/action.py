"""Player action"""


class Action(object):
    """
    Single action like:
        * take card from deck (always forced; if no cards in deck,
                               loose health points)
        * play minion card (attack; against whom?)
        * play curse / magic card
        * put minion on field (max. 7 on field)
    """
    pass


class Turn(object):
    """
    list(Action)
    """
    pass
