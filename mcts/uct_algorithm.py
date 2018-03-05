"""MCTS (UCT algorithm)"""
import random

import math

from mcts.node import Node

C_P = None


def run_uct_search(initial_state):
    v0 = Node(initial_state)
    while not stop_condition():
        v = tree_policy(v0)
        delta = default_policy(v.state)
        backup(v, delta)

    return best_child(v0, 0).action


def stop_condition():
    raise NotImplementedError()


def tree_policy(v):
    while not v.is_leaf():
        if not v.is_fully_expanded():
            return expand(v)
        else:
            v = best_child(v, C_P)

    return v


def expand(v):
    action = random.choice(v.actions)

    state_p = simulation(v.state, action)
    v_p = Node(state_p)
    v_p.action = action

    return v_p


def simulation(state, action):
    raise NotImplementedError()


def best_child(v, c):
    value = 0
    child = None

    for c in v.children:
        curr_val = (c.reward / c.visited) + \
                   c * math.sqrt(2 * math.log(v.visited) / c.visited)
        if curr_val > value:
            value = curr_val
            child = c

    return child


def default_policy(s):
    while not s.is_terminal_state():
        action = random.choice(get_possible_actions(s))
        s = simulation(s, action)

    return calculate_reward(s)


def get_possible_actions(state):
    raise NotImplementedError()


def calculate_reward(state):
    raise NotImplementedError()


def backup(v, delta):
    while v is not None:
        v.visited += 1
        v.reward += delta
        delta *= -1
        v = v.parent
