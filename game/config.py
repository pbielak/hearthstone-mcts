"""Common game configuration"""
from collections import namedtuple

from game.player.real import RealPlayer

# TODO: read from file


Config = namedtuple('Config', [
    'INITIAL_MANA',
    'INITIAL_HEALTH',
    'MAX_MINIONS',
    'player_A_cls',
    'player_B_cls'
])


def load_cfg():
    cfg = Config(
        INITIAL_HEALTH=20,
        INITIAL_MANA=1,
        MAX_MINIONS=7,
        player_A_cls=RealPlayer,
        player_B_cls=RealPlayer
    )
    return cfg
