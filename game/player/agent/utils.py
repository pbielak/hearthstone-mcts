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


def choose_best_action(mode, player, possible_actions):
    best_action = None

    for action in possible_actions:

        if best_action is None:
            best_action = action
        else:
            _, current_action_args = action
            _, best_action_args = best_action

            if mode == 'controlling':
                if player.cards[current_action_args[0]].controlling > \
                        player.cards[best_action_args[0]].controlling:
                    best_action = action
            elif mode == 'aggressive':
                if player.cards[current_action_args[0]].aggresive > \
                        player.cards[best_action_args[0]].aggresive:
                    best_action = action

    return best_action
