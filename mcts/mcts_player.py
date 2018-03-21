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
        print(game_state.player_A.name, ':',
              game_state.player_A.health, 'vs',
              game_state.player_B.name, ':',
              game_state.player_B.health)

        # Check if can perform any actions
        pa = utils.get_possible_actions(game_state)

        if pa['no_actions']:
            print(MCTSPlayer.__name__, 'chose END_TURN')
            return

        nb_actions = len(pa['spell_plays']) + \
                     len(pa['minion_puts']) + len(pa['minion_plays'])

        if nb_actions == 1:
            pas = [*pa['spell_plays'], *pa['minion_plays'], *pa['minion_puts']]

            func, args = pas[0]
            func(*args)

            print('MCTS had only one available action and executed it:', pas[0])
            return

        alg = UCTSearchAlgorithm(calling_player_name=self.name,
                                 time_limit=30)
        turn, expected_reward = alg.run(deepcopy(game_state))

        if turn is None:
            print('End of game! Terminal state!')

        print('MCTS chose turn (with expected reward:',
              expected_reward, '):', turn)

        # Update game_state
        game_state.player_A = turn.game_state.player_A
        game_state.player_B = turn.game_state.player_B
        game_state.curr_step = turn.game_state.curr_step - 1

    def __repr__(self):
        return "MCTSPlayer"
