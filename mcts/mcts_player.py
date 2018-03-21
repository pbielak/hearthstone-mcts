"""
Implementation for MCTS-based Hearthstone player
"""
from copy import deepcopy

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

        nb_spell_plays = len(pa['spell_plays'])
        nb_minion_puts = len(pa['minion_puts'])
        nb_minion_plays = len(pa['minion_plays'])
        nb_actions = nb_spell_plays + nb_minion_puts + nb_minion_plays

        if pa['no_actions']:
            print(MCTSPlayer.__name__, 'chose END_TURN')
            return

        if nb_actions == 1:
            if nb_spell_plays == 1:
                chosen_action = pa['spell_plays'][0]
            elif nb_minion_puts == 1:
                chosen_action = pa['minion_puts'][0]
            elif nb_minion_plays == 1:
                chosen_action = pa['minion_plays'][0]
            else:
                raise ValueError("Should not occur!")

            func, args = chosen_action
            func(*args)

            print('MCTS had only one available action and executed it:',
                  chosen_action)
            return

        alg = UCTSearchAlgorithm(calling_player_name=self.name,
                                 time_limit=30)
        turn, expected_reward = alg.run(deepcopy(game_state))
        print('MCTS chose turn (with expected reward:',
              expected_reward, '):', turn)

        # Update game_state
        game_state.player_A = turn.game_state.player_A
        game_state.player_B = turn.game_state.player_B
        game_state.curr_step = turn.game_state.curr_step - 1

    def __repr__(self):
        return "MCTSPlayer"
