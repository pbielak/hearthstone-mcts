"""Agent utils"""
from game import config


def score_field(player):
    """Sum of (attack, health) of each minion on field"""
    score = 0
    for minion in player.minions:
        score += minion.health + minion.attack

    return score


def perform_action(cls, chosen_action):
    func, args = chosen_action
    func(*args)

    if config.VERBOSE and cls is not None:
        print(cls.__name__, 'chose', chosen_action)


def get_best_action(actions, action_score_fn):
    best_action = None
    best_action_score = -99999

    for action in actions:
        curr_score = action_score_fn(action)
        if curr_score > best_action_score:
            best_action = action
            best_action_score = curr_score

    return best_action


def action_to_card(action, player):
    _, args = action
    card_idx = args[0]
    return player.cards[card_idx]
