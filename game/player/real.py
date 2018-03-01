"""Real player"""
from functools import partial

from game.action import take_card, play_spell, play_minion, put_minion, \
    can_use_card
from game.cards.card import SpellCard
from game.player.base import BasePlayer


class RealPlayer(BasePlayer):
    def __init__(self, name, cfg):
        super(RealPlayer, self).__init__(name, cfg)

    def get_turn(self, game_state):
        # from console (implement simple logic; keywords: input(), print())

        player_turn = []

        while True:
            action_str = "Player {name}, get action:".format(name=self.name)
            action = input(action_str)

            player_turn.append(partial(take_card, self.name))

            if action == 'PLAY_SPELL':
                print("Available spell cards:")
                for card_idx, card in enumerate(self.cards):
                    if isinstance(card, SpellCard):
                        print(card_idx, "=>", card)

                action_idx = int(input("Choose spell card to use:"))
                if can_use_card(self.name, self.cards[action_idx], game_state):
                    player_turn.append(partial(play_spell, self.name,
                                               action_idx))
                else:
                    print("Can not use card, because mana is too low...")
            elif action == 'PUT_MINION':
                player_turn.append(partial(put_minion, self.name, 0))
            elif action == 'PLAY_MINION':
                player_turn.append(partial(play_minion, self.name, 0, None))
            elif action == 'END_TURN':
                break

        return player_turn
