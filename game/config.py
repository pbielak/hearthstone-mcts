"""Common game configuration"""
from collections import namedtuple

# TODO: read from file


Config = namedtuple('Config', [
    'INITIAL_MANA',
    'INITIAL_HEALTH',
])

cfg = Config(
    INITIAL_HEALTH=20,
    INITIAL_MANA=1
)

