"""Hearthstone game state"""
from game import config
from game.player import utils


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self):
        self.player_A = utils.create_player_from_default_config(
            config.PLAYER_A_CLS, 'Pyjter'
        )
        self.player_B = utils.create_player_from_default_config(
            config.PLAYER_B_CLS, 'Mati'
        )
        self.curr_step = 0

    def is_terminal_state(self):
        """Check if game is over (one player lost)"""
        return self.player_A.is_dead() or self.player_B.is_dead()

    def get_winning_player(self):
        """Return player that won the game"""

        if self.player_A.is_dead():
            return self.player_B
        elif self.player_B.is_dead():
            return self.player_A
        else:
            assert not self.is_terminal_state()
            raise ValueError('Do not call get_winning_player '
                             'before terminal state')

    def __repr__(self):
        return "GameState"
