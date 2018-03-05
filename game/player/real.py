"""Real player"""
from game.action import play_spell, play_minion, put_minion
from game.cards.card import SpellCard, MinionCard
from game.cards.utils import get_players
from game.gui.gui_preparer import prepare_state
from game.player.base import BasePlayer
from game.player.utils import get_card_to_use, can_use_card, \
    can_put_minion, cleanup_all_dead_minions


class RealPlayer(BasePlayer):
    def __init__(self, name, cfg):
        super(RealPlayer, self).__init__(name, cfg)

    def play_turn(self, game_state):
        while True:
            print(prepare_state(game_state, self.cfg))

            action_str = "Player {name}, get one action from listed below:\n" \
                         "'PUT_MINION', 'PLAY_MINION', " \
                         "'PLAY_SPELL', 'END_TURN':"\
                .format(name=self.name)
            action = input(action_str)

            if action == 'PLAY_SPELL':
                self._play_spell(game_state)
            elif action == 'PUT_MINION':
                self._put_minion(game_state)
            elif action == 'PLAY_MINION':
                self._play_minion(game_state)
            elif action == 'END_TURN':
                break

            cleanup_all_dead_minions(game_state)

    def _play_spell(self, game_state):
        card_idx = get_card_to_use(self.cards, SpellCard)
        if can_use_card(self.name, self.cards[card_idx], game_state):
            play_spell(self, card_idx, game_state)
        else:
            print("Cannot use this card...")

    def _put_minion(self, game_state):
        card_idx = get_card_to_use(self.cards, MinionCard)
        if can_use_card(self.name, self.cards[card_idx], game_state) \
                and can_put_minion(self.name, game_state, self.cfg):
            put_minion(self, card_idx)
        else:
            print("Cannot put minion...")

    def _play_minion(self, game_state):
        card_idx = get_card_to_use(self.minions, MinionCard)
        if self.minions[card_idx].can_attack:

            _, opponent = get_players(game_state, self)
            choice = input('Get target [ENEMY_PLAYER, ENEMY_MINION]:')
            if choice == 'ENEMY_PLAYER':
                target = opponent
            elif choice == 'ENEMY_MINION':
                print('Enemy minions:')
                for idx, minion in enumerate(opponent.minions):
                    print(idx, '=>', minion)
                chosen_idx = int(input('Get idx:'))
                target = opponent.minions[chosen_idx]
            else:
                return

            play_minion(self, card_idx, target, game_state)
        else:
            print('Cannot play minion...')
