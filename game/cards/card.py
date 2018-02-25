"""Base Card class"""


class Card(object):
    """Base class for all cards
    """
    def __init__(self):
        pass

    def apply(self, game_state):
        """
        This method should be implemented in all classes, which inherit from
        this class. It should take the current game state, perform a deepcopy,
        modify the copy (according to the effect of the actual card) and return
        the modified game state.

        :param game_state: current game state, should NOT be modified directly
        :return: modified copy of input game state
        """
        pass
