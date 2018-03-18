"""All available cards"""
from copy import deepcopy
import random

from game.cards import card as cards
from game.player import utils

ALL_CARDS = []


def get_all_available_cards():
    return list(map(lambda x: deepcopy(x), ALL_CARDS))


###################################################
# ---------------- MINIONS CARDS ---------------- #
###################################################

# NO SIDE-EFFECT
ALL_CARDS.extend([
    cards.MinionCard(name="Enchanted Raven",
                     health=2,
                     attack=2,
                     cost=1,
                     side_effect=None),
    cards.MinionCard(name="Spider Tank",
                     health=4,
                     attack=3,
                     cost=3,
                     side_effect=None),
    cards.MinionCard(name="Ice Rager",
                     health=2,
                     attack=5,
                     cost=3,
                     side_effect=None),
    cards.MinionCard(name="Worgen Greaser",
                     health=3,
                     attack=6,
                     cost=4,
                     side_effect=None),
    cards.MinionCard(name="Am'gam Rager",
                     health=5,
                     attack=1,
                     cost=3,
                     side_effect=None),
])

# WITH SIDE-EFFECT


def restore_health_for_minions(game_state, source, target):
    """For each enemy minion, restore 2 Health to your hero."""

    player, opponent = utils.get_players(game_state, source)

    # Health is hard-coded to 20 as there is a problem with import-cycles :C
    player.health = min(20, player.health + 2 * len(opponent.minions))


def reduce_enemy_minions_attack_points(game_state, source, target):
    """Change all enemy minions' attack to 1."""

    _, opponent = utils.get_players(game_state, source)

    for minion in opponent.minions:
        minion.attack = 1


ALL_CARDS.extend([
    cards.MinionCard(name="Cult Apothecary",
                     health=4,
                     attack=4,
                     cost=5,
                     side_effect=restore_health_for_minions),
    cards.MinionCard(name="Eadric the Pure",
                     health=7,
                     attack=3,
                     cost=7,
                     side_effect=reduce_enemy_minions_attack_points),
])


###################################################
# ----------------- SPELL CARDS ----------------- #
###################################################

def deal_damage_to_enemy_minions(game_state, source, target):
    """Deal 4 damage to all enemy minions."""

    _, opponent = utils.get_players(game_state, source)

    for minion in opponent.minions:
        minion.health -= 4


def draw_cards(game_state, source, target):
    """Draw 4 cards."""

    player, _ = utils.get_players(game_state, source)

    for _ in range(4):
        if player.deck.is_empty():
            player.deck.no_attempt_pop_when_empty += 1
            player.health -= player.deck.no_attempt_pop_when_empty
        else:
            card = player.deck.pop()
            player.cards.append(card)


def deal_damage_to_all_enemies(game_state, source, target):
    """Deal 2 damage to all enemies."""

    _, opponent = utils.get_players(game_state, source)

    opponent.health -= 2

    for minion in opponent.minions:
        minion.health -= 2


ALL_CARDS.extend([
    cards.SpellCard(name="Flamestrike",
                    cost=7,
                    effect=deal_damage_to_enemy_minions),
    cards.SpellCard(name="Sprint",
                    cost=7,
                    effect=draw_cards),
    cards.SpellCard(name="Consecration",
                    cost=4,
                    effect=deal_damage_to_all_enemies),
])
