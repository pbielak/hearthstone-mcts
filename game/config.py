"""Common game configuration"""
from collections import namedtuple

from game.player.agent.random import RandomAgent
from game.player.real import RealPlayer


Config = namedtuple('Config', [
    'INITIAL_MANA',
    'INITIAL_HEALTH',
    'MAX_MINIONS',
    'MAX_MANA',
    'player_A_cls',
    'player_B_cls'
])


def load_cfg():
    cfg = Config(
        INITIAL_HEALTH=20,
        INITIAL_MANA=0,
        MAX_MINIONS=7,
        MAX_MANA=10,
        player_A_cls=RealPlayer,
        player_B_cls=RandomAgent
    )
    return cfg
