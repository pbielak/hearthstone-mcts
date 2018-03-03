"""Real player"""
from functools import partial

from game.action import play_spell, play_minion, put_minion
from game.cards.card import SpellCard, MinionCard
from game.player.base import BasePlayer
from game.player.utils import get_card_to_use, can_use_card, can_put_minion


class RealPlayer(BasePlayer):
    def __init__(self, name, cfg):
        super(RealPlayer, self).__init__(name, cfg)

    def get_turn(self, game_state):
        player_turn = []

        while True:
            action_str = "Player {name}, get action [PUT_MINION, " \
                         "PLAY_MINION, PLAY_SPELL, END_TURN]:"\
                .format(name=self.name)
            action = input(action_str)

            if action == 'PLAY_SPELL':
                card_idx = get_card_to_use(self.cards, SpellCard, "play")
                if can_use_card(self.name, self.cards[card_idx], game_state):
                    player_turn.append(partial(play_spell, self.name, card_idx))
                else:
                    print("Can not use this card...")
            elif action == 'PUT_MINION':
                card_idx = get_card_to_use(self.cards, MinionCard, "put")
                if can_put_minion(self.name, game_state, self.cfg):
                    player_turn.append(partial(put_minion, self.name, card_idx))
                else:
                    print("Can not put (specified) minion...")
            elif action == 'PLAY_MINION':
                card_idx = get_card_to_use(self.minions, MinionCard, "play")
                if can_use_card(self.name, self.minions[card_idx], game_state):
                    # TODO: get target
                    player_turn.append(
                        partial(play_minion, self.name, card_idx, None))
            elif action == 'END_TURN':
                break

        return player_turn
