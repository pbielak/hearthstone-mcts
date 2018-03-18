"""Random agent

Randomly choose actions
"""
import random

from game.player import base
from game.player.agent import utils as ag_utils
from game.player import utils as pl_utils


class RandomAgent(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(RandomAgent, self).__init__(name, health, mana, already_used_mana,
                                          deck, cards, minions)

    def play_turn(self, game_state):
        while True:
            possible_actions = pl_utils.get_possible_actions(game_state, self)

            if possible_actions['no_actions']:
                print(RandomAgent.__name__, 'chose END_TURN')
                break

            pa = (*possible_actions['spell_plays'],
                  *possible_actions['minion_plays'],
                  *possible_actions['minion_puts'])

            chosen_action = random.choice(pa)
            ag_utils.perform_action(RandomAgent, chosen_action)

            pl_utils.cleanup_all_dead_minions(game_state)
