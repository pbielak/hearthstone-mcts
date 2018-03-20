"""
Implementation for MCTS-based Hearthstone player
"""
from game.player import base


class MCTSPlayer(base.BasePlayer):
    def __init__(self, name, health, mana, already_used_mana,
                 deck, cards, minions):
        super(MCTSPlayer, self).__init__(name, health, mana, already_used_mana,
                                         deck, cards, minions)

    def play_turn(self, game_state):
        pass  # Run the UCT algorithm, get action (turn) and apply it

    def __repr__(self):
        return "MCTSPlayer"
