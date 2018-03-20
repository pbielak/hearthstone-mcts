"""
Implementation for MCTS-based Hearthstone player
"""
from copy import deepcopy

from game import config
from game.player import base
from game.player import utils
from mcts.uct_algorithm import UCTSearchAlgorithm


class MCTSPlayer(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(MCTSPlayer, self).__init__(name, health, mana, already_used_mana,
                                         deck, cards, minions)

    def play_turn(self, game_state):
        # Check if can perform any actions
        pa = utils.get_possible_actions(game_state)
        if pa['no_actions']:
            print(MCTSPlayer.__name__, 'chose END_TURN')
            return

        alg = UCTSearchAlgorithm(calling_player_name=self.name,
                                 time_limit=15)
        turn = alg.run(deepcopy(game_state))
        print('MCTS CHOSE FINAL TURN:', turn)

        # Update game_state
        game_state.player_A = turn.game_state.player_A
        game_state.player_B = turn.game_state.player_B
        game_state.curr_step = turn.game_state.curr_step - 1

    def __repr__(self):
        return "MCTSPlayer"
