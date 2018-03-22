"""
Stats component
"""
import time

import numpy as np

from mcts.node import DrawCardNode, DecisionTurnNode


instance = None


def get_instance():
    global instance
    assert instance is not None

    return instance


class StatsCounter(object):
    def __init__(self, filename):
        print('Stats saved to:', filename)
        self.fh = open('experiment/{}'.format(filename), 'w')
        self.nodes = []

        self.fh.write('#timestamp;nb_simulations;avg_children;'
                      'max_depth;avg_depth;median_depth\n')
        self.fh.flush()

    def push_node(self, node):
        self.nodes.append(node)

    def commit_data(self):
        data = self._collect_data()
        data_str = '{};{};{};{};{};{}\n'.format(
            time.time(),
            data['nb_simulation'],
            round(data['avg_children'] * 100, 3),
            data['max_depth'],
            round(data['avg_depth'], 3),
            data['median_depth'],
        )

        self.fh.write(data_str)
        self.fh.flush()

    def _collect_data(self):
        data = dict()
        data['nb_simulation'] = self.nodes[0].visited

        leaf_depths = []
        children_percs = []

        for node in self.nodes:
            if isinstance(node, DrawCardNode):
                children_perc = 1 - (node.children.count(None) / len(node.children))
                leaf_depth = None
            elif isinstance(node, DecisionTurnNode):
                nb_children = len(node.children)
                nb_turns = len(node.turns)

                if nb_turns == 0 and nb_children == 0:
                    children_perc = 0
                else:
                    children_perc = nb_children / (nb_children + nb_turns)
                leaf_depth = node.depth if len(node.children) == 0 else None
            else:
                raise ValueError("Should never happen!")

            children_percs.append(children_perc)
            if leaf_depth is not None:
                leaf_depths.append(leaf_depth)

        data['avg_children'] = np.mean(children_percs)
        data['max_depth'] = np.max(leaf_depths)
        data['avg_depth'] = np.mean(leaf_depths)
        data['median_depth'] = np.median(leaf_depths)

        return data

    def clear(self):
        self.nodes.clear()
