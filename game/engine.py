"""Game engine"""
from copy import deepcopy
from functools import partial

from game.action import take_card, set_total_mana
from game.gui.gui_preparer import prepare_state
from game.player.utils import get_current_player
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

            player = self.choose_player()

            game_state_cpy = self.create_game_state_copy(self.game_state)
            game_state_cpy = self.run_actions(player, game_state_cpy)

            print(prepare_state(game_state_cpy, self.cfg))
            turn = player.get_turn(game_state_cpy)

            self.game_state = self.apply_turn(game_state_cpy, turn)

    def on_round_begin(self):
        self.step_no += 1

    def choose_player(self):
        if self.step_no % 2 == 0:
            return self.game_state.player_A
        return self.game_state.player_B

    def run_actions(self, player, game_state):
        game_state_tmp = take_card(player.name, game_state)
        # TODO: improve by independent round counters
        game_state_tmp = set_total_mana(self.step_no, game_state_tmp)
        get_current_player(player.name, game_state_tmp)\
            .already_used_mana = 0
        return game_state_tmp

    def apply_turn(self, game_state, turn):
        for action in turn:
            game_state = action(game_state)
        return game_state

    def create_game_state_copy(self, game_state):
        return deepcopy(game_state)
