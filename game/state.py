"""Hearthstone game state"""


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self, player_A, player_B, curr_step):
        self.player_A = player_A
        self.player_B = player_B
        self.curr_step = curr_step

    def is_terminal_state(self):
        """Check if game is over (one player lost)"""
        return self.player_A.is_dead() or self.player_B.is_dead()

    def get_winning_player(self):
        """Return player that won the game"""

        if self.player_A.is_dead():
            return self.player_B
        elif self.player_B.is_dead():
            return self.player_A

        assert not self.is_terminal_state()
        raise ValueError('Do not call get_winning_player '
                         'before terminal state')

    def get_players(self):
        """Returns (current_player, opponent)"""
        if self.curr_step % 2 == 1:
            return self.player_A, self.player_B
        return self.player_B, self.player_A

    def __repr__(self):
        return "GameState"

    def __hash__(self):
        return hash((self.player_A, self.player_B, self.curr_step))

    def __eq__(self, other):
        if isinstance(other, GameState):
            return hash(self) == hash(other)
            # return self.player_A == other.player_A and \
            #        self.player_B == other.player_B and \
            #        self.curr_step == other.curr_step
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
