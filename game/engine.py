"""Game engine"""
from game.state import GameState


class GameEngine(object):
    """
    Main loop of game
    """
    def __init__(self, cfg):
        self.game_state = GameState(cfg)
        self.current_player = None  # player_A.name or player_B.name
        self.step_no = 0  # current game step number

    def run(self):
        while not self.game_state.is_terminal_state():
            pass
            # update game state (increment step_no, set current_player)
            # choose player + get turn from player
            # apply turn on game_state
