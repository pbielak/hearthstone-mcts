"""Real player"""
from game import action
from game.cards import card as cards
from game.gui import gui_preparer
from game.player import base
from game.player import utils


class RealPlayer(base.BasePlayer):
    def __init__(self, name):
        super(RealPlayer, self).__init__(name)

    def play_turn(self, game_state):
        while True:
            print(gui_preparer.prepare_state(game_state))

            # --- TODO REMOVE ---
            from pprint import pprint
            pprint(utils.get_possible_actions(game_state, self))
            # --- TODO END REMOVE ---

            action_str = "Player {name}, get one action from listed below:\n" \
                         "0. 'PUT_MINION', 1. 'PLAY_MINION', " \
                         "2. 'PLAY_SPELL', 3. 'END_TURN':"\
                .format(name=self.name)
            action = int(input(action_str))

            if action == 0:  # PUT_MINION
                self._put_minion()
            elif action == 1:  # PLAY_MINION
                self._play_minion(game_state)
            elif action == 2:  # PLAY_SPELL
                self._play_spell(game_state)
            elif action == 3:  # END_TURN
                break
            else:
                print('Unknown command!')

            utils.cleanup_all_dead_minions(game_state)

    def _play_spell(self, game_state):
        card_idx = get_card_to_use(self.cards, cards.SpellCard)
        if utils.can_use_card(self, self.cards[card_idx]):
            action.play_spell(self, card_idx, game_state)
        else:
            print("Cannot use this card...")

    def _put_minion(self):
        card_idx = get_card_to_use(self.cards, cards.MinionCard)
        if utils.can_use_card(self, self.cards[card_idx]) \
                and utils.can_put_minion(self):
            action.put_minion(self, card_idx)
        else:
            print("Cannot put minion...")

    def _play_minion(self, game_state):
        card_idx = get_card_to_use(self.minions, cards.MinionCard)
        if self.minions[card_idx].can_attack:
            target = get_target_for_minion_attack(game_state, self)
            action.play_minion(self, card_idx, target, game_state)
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


def get_target_for_minion_attack(game_state, player):
    _, opponent = utils.get_players(game_state, player)

    while True:
        choice = int(input('Get target [0. ENEMY_PLAYER, 1. ENEMY_MINION]:'))
        if choice == 0:  # ENEMY_PLAYER
            return opponent
        elif choice == 1:  # ENEMY_MINION
            print('Enemy minions:')
            for idx, minion in enumerate(opponent.minions):
                print(idx, '=>', minion)
            chosen_idx = int(input('Get idx:'))
            return opponent.minions[chosen_idx]
