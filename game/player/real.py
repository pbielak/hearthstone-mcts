"""Real player"""
from functools import partial

from game.action import take_card
from game.player.base import BasePlayer


class RealPlayer(BasePlayer):
    def __init__(self, name, cfg):
        super(RealPlayer, self).__init__(name, cfg)

    def get_turn(self, game_state):
        # TODO: should create Turn object by getting information
        # from console (implement simple logic; keywords: input(), print())

        player_turn = []

        while True:
            action_str = "Player {name}, get action:".format(name=self.name)
            action = input(action_str)

            if action == 'TAKE_CARD':
                player_turn.append(partial(take_card, self.name))
            elif action == 'END_TURN':
                break

        return player_turn
