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
            possible_actions = pl_utils.get_possible_actions(game_state)

            if possible_actions['no_actions']:
                if config.VERBOSE:
                    print(AggressiveAgent.__name__, 'chose END_TURN')
                break

            player, opponent = game_state.get_players()

            # Try to attack enemy hero
            if possible_actions['minion_plays']:
                for pa in possible_actions['minion_plays']:
                    func, args = pa
                    _, target_idx, _ = args
                    if target_idx == -1:  # -1 means opponent hero
                        ag_utils.perform_action(AggressiveAgent, pa)

                    # If enemy died end the turn (and game)
                    if opponent.is_dead():
                        return

            actions = [*possible_actions['minion_puts'],
                       *possible_actions['spell_plays']]

            # Check field
            if actions:
                if ag_utils.score_field(opponent) > ag_utils.score_field(player):

                    best_action = ag_utils.get_best_action(
                        actions,
                        lambda a: ag_utils.action_to_card(a, player).aggressive_rate)

                    ag_utils.perform_action(AggressiveAgent, best_action)
                    pl_utils.cleanup_all_dead_minions(game_state)
                else:
                    if config.VERBOSE:
                        print(AggressiveAgent.__name__, 'chose END_TURN')
                    break
