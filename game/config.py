"""Common game configuration"""
from game.player.agent.random import RandomAgent
from game.player.real import RealPlayer
from mcts.mcts_player import MCTSPlayer


INITIAL_HEALTH = 20
INITIAL_MANA = 0
MAX_MINIONS = 7
MAX_MANA = 10
PLAYER_A_CLS = MCTSPlayer
PLAYER_B_CLS = RandomAgent

VERBOSE = False
