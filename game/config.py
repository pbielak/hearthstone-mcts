"""Common game configuration"""
from collections import namedtuple

from game.player.real import RealPlayer

# TODO: read from file


Config = namedtuple('Config', [
    'INITIAL_MANA',
    'INITIAL_HEALTH',
    'player_A_cls',
    'player_B_cls'
])


def load_cfg():
    cfg = Config(
        INITIAL_HEALTH=20,
        INITIAL_MANA=1,
        player_A_cls=RealPlayer,
        player_B_cls=RealPlayer
    )
    return cfg
