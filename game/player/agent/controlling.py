"""Controlling agent

First check the state of the field, if there aren't any enemy minions,
then attack the enemy hero.
"""
from game import config
from game.player import base
from game.player.agent import utils as ag_utils
from game.player import utils as pl_utils


class ControllingAgent(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(ControllingAgent, self).__init__(name, health, mana,
                                               already_used_mana, deck,
                                               cards, minions)

    def play_turn(self, game_state):
        config.VERBOSE = True

        # ------------- Check field ----------------
        print('ControllingAgent check field')
        while True:
            possible_actions = pl_utils.get_possible_actions(game_state)

            if possible_actions['no_actions']:
                if config.VERBOSE:
                    print(ControllingAgent.__name__, 'chose END_TURN')
                break

            player, opponent = game_state.get_players()

            minion_minion_actions = []
            for pa in possible_actions['minion_plays']:
                _, args = pa
                _, target_idx, _ = args
                if target_idx != -1:
                    minion_minion_actions.append(pa)

            actions = [*possible_actions['minion_puts'],
                       *possible_actions['spell_plays'],
                       *minion_minion_actions]

            if actions and ag_utils.score_field(opponent) >= ag_utils.score_field(player):
                best_action = ag_utils.get_best_action(
                    actions,
                    lambda a: ag_utils.action_to_card(a, player).controlling_rate)

                ag_utils.perform_action(ControllingAgent, best_action)
            else:
                if config.VERBOSE:
                    print(ControllingAgent.__name__, 'chose END_TURN')
                break

        # ------------- Attack -----------------
        print('ControllingAgent attack')
        while True:
            possible_actions = pl_utils.get_possible_actions(game_state)

            if possible_actions['no_actions']:
                if config.VERBOSE:
                    print(ControllingAgent.__name__, 'chose END_TURN')
                break

            player, opponent = game_state.get_players()

            actions = possible_actions['minion_plays']

            if actions:
                # Try to attack enemy hero, if no enemy minions
                if not opponent.minions:
                    for pa in actions:
                        func, args = pa
                        _, target_idx, _ = args
                        if target_idx == -1:  # -1 means opponent hero
                            ag_utils.perform_action(ControllingAgent, pa)

                            # If enemy died end the turn (and game)
                            if opponent.is_dead():
                                return

                            break

                # There are enemy minions
                else:
                    for pa in actions:
                        func, args = pa
                        _, target_idx, _ = args
                        if target_idx != -1:
                            ag_utils.perform_action(ControllingAgent, pa)
                            pl_utils.cleanup_all_dead_minions(game_state)
                            break
            else:
                if config.VERBOSE:
                    print(ControllingAgent.__name__, 'chose END_TURN')
                break

        pl_utils.cleanup_all_dead_minions(game_state)
