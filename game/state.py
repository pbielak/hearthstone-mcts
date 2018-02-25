"""Hearthstone game state"""


class GameState(object):
    """
    Player A <--- CardDeck A
    Player B <--- CardDeck B
    Current turn [player A or player B]
    """
    def __init__(self):
        self.player_A = None
        self.card_deck_A = None
        self.player_B = None
        self.card_deck_B = None
        self.current_player = None  # player_A.name or player_B.name
        self.step_no = None  # current game step number

    def is_terminal_state(self):
        pass

