"""Hearthstone game state"""


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    """
    def __init__(self, cfg):
        self.player_A = cfg.player_A_cls('Pyjter', cfg)
        self.player_B = cfg.player_B_cls('Mati', cfg)

    def is_terminal_state(self):
        """Check if game is over (one player lost)"""
        is_player_A_dead = self.player_A.health <= 0
        is_player_B_dead = self.player_B.health <= 0
        return is_player_A_dead or is_player_B_dead

    def __repr__(self):
        fmt_str = "GameState: Player A: {player_A}; \n" \
                  "Deck A: {deck_A}; \n" \
                  "Player B: {player_B}; \n" \
                  "Deck B: {deck_B};\n"

        return fmt_str.format(player_A=self.player_A,
                              deck_A=self.player_A.deck,
                              player_B=self.player_B,
                              deck_B=self.player_B.deck)
