"""MCTS (UCT algorithm)"""
import math

from mcts.node import DecisionTurnNode, DrawCardNode
from mcts.simulation import simulate_random_game as simulation
from mcts import utils
from mcts.turn import TurnGenerator


class UCTSearchAlgorithm(object):
    def __init__(self, calling_player_name,
                 time_limit=30,
                 coeff=1.0/math.sqrt(2)):
        self.calling_player_name = calling_player_name
        self.timer = utils.Timer(time_limit)
        self.coeff = coeff

    def stop_condition(self):
        return self.timer.time_limit_exceeded()

    def run(self, initial_state):
        """Gets INITIAL_STATE and
        returns best TURN to take
        in this state."""
        self.timer.start()

        turns = TurnGenerator().generate_all_turns(initial_state)
        root_node = DecisionTurnNode(state=initial_state,
                                     parent=None,
                                     turns=turns)

        while not self.stop_condition():
            node = self.select_node(root_node)
            print('Selected node:', node)

            reward = simulation(node.state)
            print('Simulation - got reward:', reward)

            self.backpropagation(node, reward)

        return root_node.get_best_child(0).turn

    def select_node(self, root_node):
        node = root_node
        while not node.is_terminal():
            if not node.is_fully_expanded():
                return node.expand()
            else:
                node = node.get_best_child(self.coeff)

        return node

    def backpropagation(self, node, reward):
        prev_node = None
        current_node = node
        reward_update = 0

        while current_node is not None:
            current_node.visited += 1

            if isinstance(current_node, DrawCardNode):
                # Find from which child we got here
                child_idx = -1
                for idx, child in enumerate(current_node.children):
                    if child.id == prev_node.id:
                        child_idx = idx
                        break
                assert child_idx != -1

                prob = current_node.probs[child_idx]
                reward_update = prob * reward

            elif isinstance(current_node, DecisionTurnNode):
                reward_update = reward

            # Based on player assigned to node game_state,
            # update properly reward
            current_player, _ = current_node.state.get_players()
            if self.calling_player_name == current_player.name:
                current_node.reward += reward_update
            else:
                current_node.reward -= reward_update
            prev_node, current_node = current_node, current_node.parent
