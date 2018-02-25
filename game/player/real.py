"""Real player"""
from game.player.base import BasePlayer


class RealPlayer(BasePlayer):
    def __init__(self, name, cfg):
        super(RealPlayer, self).__init__(name, cfg)

    def get_turn(self, game_state):
        # TODO: should create Turn object by getting information
        # from console (implement simple logic; keywords: input(), print())
        raise NotImplementedError()
