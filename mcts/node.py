"""MCTS Tree Node"""


class Node(object):
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.children = []
        self.actions = []
        self.action = None

        self.visited = 0
        self.reward = 0

    def is_leaf(self):
        return not self.children

    def is_fully_expanded(self):
        return not self.actions

    def __repr__(self):
        fmt_str = "Node(" \
                  "S: {state}," \
                  "P: {parent}," \
                  "C: {children})"

        return fmt_str.format(state=self.state,
                              parent=self.parent,
                              children=self.children)