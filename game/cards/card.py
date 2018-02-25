"""Base Card class"""


class Card(object):
    """Base class for all cards
    """
    def __init__(self):
        pass

    def apply(self, game_state, calling_player, target_player):
        """
        This method should be implemented in all classes, which inherit from
        this class. It should take the current game state, perform a deepcopy,
        modify the copy (according to the effect of the actual card) and return
        the modified game state.

        :param game_state: current game state, should NOT be modified directly
        :param calling_player: the player which called this card
        :param target_player: the targeted player (if card does not need
                              a target; like updating the stats of the current
                              player, then assume that target_player = None)
        :return: modified copy of input game state
        """
        pass


# TODO: think about constructor parameters (for base class, AbilityCard and MinionCard)


class AbilityCard(Card):
    pass


class MinionCard(Card):
    pass
