"""Hearthstone game state"""


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self, cfg):
        self.player_A = cfg.player_A_cls('Pyjter', cfg)
        self.player_B = cfg.player_B_cls('Mati', cfg)
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
        # fmt_str = "GameState: Player A: {player_A}; \n" \
        #           "Deck A: {deck_A}; \n" \
        #           "Player B: {player_B}; \n" \
        #           "Deck B: {deck_B};\n"
        #
        # return fmt_str.format(player_A=self.player_A,
        #                       deck_A=self.player_A.deck,
        #                       player_B=self.player_B,
        #                       deck_B=self.player_B.deck)
        return "GameState"
