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
            self.on_round_begin()
            player = self.choose_player()
            turn = self.get_player_turn(player)
            self.game_state = self.apply_turn(turn)

    def on_round_begin(self):
        pass

    def choose_player(self):
        pass

    def get_player_turn(self, player):
        pass

    def apply_turn(self, turn):
        pass
