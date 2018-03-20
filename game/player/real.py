"""Real player"""
from game import action
from game.cards.card import MinionCard, SpellCard
from game.player import base
from game.player import utils


class RealPlayer(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(RealPlayer, self).__init__(name, health, mana, already_used_mana,
                                         deck, cards, minions)

    def play_turn(self, game_state):
        while True:
            # --- TODO REMOVE ---
            from game import config
            from game.gui import gui_preparer

            if config.VERBOSE:
                # Will double the gui output (but will show the state after
                # each action of the RealPlayer)
                print(gui_preparer.prepare_state(game_state))

            from pprint import pprint
            pprint(utils.get_possible_actions(game_state))

            from mcts.turn import TurnGenerator
            from copy import deepcopy
            turns = TurnGenerator().generate_all_turns(deepcopy(game_state))
            print(turns)
            print(len(turns))

            # --- TODO END REMOVE ---

            action_str = "Player {name}, get one action from listed below:\n" \
                         "0. 'PUT_MINION', 1. 'PLAY_MINION', " \
                         "2. 'PLAY_SPELL', 3. 'END_TURN':"\
                .format(name=self.name)
            action = int(input(action_str))

            if action == 0:  # PUT_MINION
                self._put_minion(game_state)
            elif action == 1:  # PLAY_MINION
                self._play_minion(game_state)
            elif action == 2:  # PLAY_SPELL
                self._play_spell(game_state)
            elif action == 3:  # END_TURN
                break
            else:
                print('Unknown command!')

            utils.cleanup_all_dead_minions(game_state)
            if game_state.is_terminal_state():
                break

    def _play_spell(self, game_state):
        card_idx = get_card_to_use(self.cards, SpellCard)
        if utils.can_use_card(self, self.cards[card_idx]):
            action.play_spell(card_idx, game_state)
        else:
            print("Cannot use this card...")

    def _put_minion(self, game_state):
        card_idx = get_card_to_use(self.cards, MinionCard)
        if utils.can_use_card(self, self.cards[card_idx]) \
                and utils.can_put_minion(self):
            action.put_minion(card_idx, game_state)
        else:
            print("Cannot put minion...")

    def _play_minion(self, game_state):
        card_idx = get_card_to_use(self.minions, MinionCard)
        if self.minions[card_idx].can_attack:
            target_idx = get_target_for_minion_attack(game_state)
            action.play_minion(card_idx, target_idx, game_state)
        else:
            print('Cannot play minion...')


def get_card_to_use(cards_list, cls):
    info_fmt_str = "Available {card_type}s:".format(card_type=cls.__name__)
    action_fmt_str = "Choose one card:"
    print(info_fmt_str)

    for card_idx, card in enumerate(cards_list):
        if isinstance(card, cls):
            print(card_idx, "=>", card)

    choice = int(input(action_fmt_str))
    if isinstance(cards_list[choice], cls):
        return choice
    else:
        raise ValueError("Incorrect card index...")


def get_target_for_minion_attack(game_state):
    _, opponent = game_state.get_players()

    while True:
        choice = int(input('Get target [0. ENEMY_PLAYER, 1. ENEMY_MINION]:'))
        if choice == 0:  # ENEMY_PLAYER => -1
            return -1
        elif choice == 1:  # ENEMY_MINION => 0...x (index)
            print('Enemy minions:')
            for idx, minion in enumerate(opponent.minions):
                print(idx, '=>', minion)
            chosen_idx = int(input('Get idx:'))
            return chosen_idx
