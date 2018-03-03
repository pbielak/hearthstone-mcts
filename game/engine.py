"""Game engine"""
from copy import deepcopy
from functools import partial

from game.action import take_card, set_total_mana
from game.gui.gui_preparer import prepare_state
from game.state import GameState


class GameEngine(object):
    """Object implementing main loop / logic of game

    Attributes:
        * game_state (GameState): the current game state
        * step_no (int): current game step number
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.game_state = GameState(cfg)
        self.step_no = 0

    def run(self):
        while not self.game_state.is_terminal_state():
            self.on_round_begin()
            print(prepare_state(self.game_state, self.cfg))
            player = self.choose_player()
            turn = player.get_turn(self.game_state)

            self.game_state = self.apply_turn(self.game_state, turn)

    def on_round_begin(self):
        self.step_no += 1

    def choose_player(self):
        if self.step_no % 2 == 0:
            return self.game_state.player_A
        return self.game_state.player_B

    def apply_turn(self, game_state, turn):
        game_state_cpy = deepcopy(game_state)
        for action in turn:
            game_state_cpy = action(game_state_cpy)
        return game_state_cpy
