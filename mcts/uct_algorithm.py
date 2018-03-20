"""MCTS (UCT algorithm)"""
import math
import random

from mcts.node import DecisionTurnNode, DrawCardNode
from mcts.simulation import simulate_random_game as simulation
from mcts import utils


class UCTSearchAlgorithm(object):
    def __init__(self, time_limit=30, coeff=math.sqrt(2)):
        self.timer = utils.Timer(time_limit)
        self.coeff = coeff

    def stop_condition(self):
        return self.timer.time_limit_exceeded()

    def run(self, initial_state):
        """Gets INITIAL_STATE and
        returns best TURN to take
        in this state."""
        self.timer.start()

        root_node = DecisionTurnNode(state=initial_state,
                                     parent=None)

        while not self.stop_condition():
            node = self.select_node(root_node)
            reward = simulation(node.state)
            self.backpropagation(node, reward)

        return self.best_child(root_node, 0).turn

    def select_node(self, root_node):
        node = root_node
        while not node.is_terminal():
            if not node.is_fully_expanded():
                return self.expand(node)
            else:
                node = self.best_child(node, self.coeff)

        return node

    def backpropagation(self, node, reward):
        pass

    def best_child(self, node, coeff):
        pass

    def expand(self, node):
        pass


# C_P = None
#

#
#
# def expand(v):
#     action = random.choice(v.actions)
#
#     state_p = simulation(v.state, action)
#     v_p = Node(state_p)
#     v_p.action = action
#
#     return v_p
#
#
# def best_child(v, c):
#     value = 0
#     child = None
#
#     for c in v.children:
#         curr_val = (c.reward / c.visited) + \
#                    c * math.sqrt(2 * math.log(v.visited) / c.visited)
#         if curr_val > value:
#             value = curr_val
#             child = c
#
#     return child
#
#
# def backup(v, delta):
#     while v is not None:
#         v.visited += 1
#         v.reward += delta
#         delta *= -1
#         v = v.parent
