"""Aggressive agent

First attack the enemy hero, then check the field.
"""
from game import config
from game.player import base
from game.player.agent import utils as ag_utils
from game.player import utils as pl_utils


class AggressiveAgent(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(AggressiveAgent, self).__init__(name, health, mana,
                                              already_used_mana, deck,
                                              cards, minions)

    def play_turn(self, game_state):
        while True:
            possible_actions = pl_utils.get_possible_actions(game_state, self)

            if possible_actions['no_actions']:
                if config.VERBOSE:
                    print(AggressiveAgent.__name__, 'chose END_TURN')
                break

            player, opponent = pl_utils.get_players(game_state, self)

            # Try to attack enemy hero
            if possible_actions['minion_plays']:
                for pa in possible_actions['minion_plays']:
                    func, args = pa
                    _, _, target, _ = args
                    if target is opponent:
                        ag_utils.perform_action(AggressiveAgent, pa)

                    # If enemy died end the turn (and game)
                    if opponent.is_dead():
                        return

            # Check field
            # TODO: select best minion AND use spells!
            if possible_actions['minion_puts'] and \
                ag_utils.score_field(opponent) > ag_utils.score_field(player):
                ag_utils.perform_action(AggressiveAgent,
                                        possible_actions['minion_puts'][0])

            pl_utils.cleanup_all_dead_minions(game_state)
