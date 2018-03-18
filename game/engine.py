"""Game engine"""
from copy import deepcopy

from game.action import take_card, increment_mana
from game.state import GameState


class GameEngine(object):
    """Object implementing main loop / logic of game

    Attributes:
        * game_state (GameState): the current game state
        * cfg (Config): common configuration of the game
    """
    def __init__(self, cfg):
        self.cfg = cfg
        self.game_state = GameState(cfg)

    def run(self):
        self.prepare_game()

        while not self.game_state.is_terminal_state():
            self.game_state.curr_step += 1
            game_state_cpy = deepcopy(self.game_state)

            player = self.choose_player(game_state_cpy)
            game_state_cpy = self.prepare_player(player, game_state_cpy)
            player.play_turn(game_state_cpy)

            self.game_state = game_state_cpy

        winning_player = self.game_state.get_winning_player()
        print('Player {} won the game!'.format(winning_player.name))

    @staticmethod
    def choose_player(game_state):
        if game_state.curr_step % 2 == 1:
            return game_state.player_A
        return game_state.player_B

    def prepare_player(self, player, game_state):
        take_card(player)
        increment_mana(self.cfg, player)
        player.already_used_mana = 0

        for minion in player.minions:
            minion.can_attack = True

            if minion.side_effect is not None:
                minion.side_effect(game_state, player, None)

        return game_state

    def prepare_game(self):
        for _ in range(3):
            take_card(self.game_state.player_A)

        for _ in range(4):
            take_card(self.game_state.player_B)
