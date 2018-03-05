"""Agent utils"""


def score_field(player):
    """Sum of (attack, health) of each minion on field"""
    score = 0
    for minion in player.minions:
        score += minion.health + minion.attack

    return score


def perform_action(cls, chosen_action):
    func, args = chosen_action
    func(*args)
    print(cls.__name__, 'chose', chosen_action)