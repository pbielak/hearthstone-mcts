"""Player action"""
from copy import deepcopy
from game.player.utils import get_current_player

# Single action like:
#     * take card from deck (always forced; if no cards in deck,
#                            loose health points)
#     * play minion card (attack; against whom?)
#     * play curse / magic card
#     * put minion on field (max. 7 on field)

#######
# Actions called by system
#######


def set_total_mana(mana, game_state):
    game_state_cpy = deepcopy(game_state)
    game_state_cpy.player_A.mana += mana
    game_state_cpy.player_B.mana += mana
    return game_state_cpy


def take_card(player_name, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    if not current_player.deck.is_empty():
        current_player.cards.append(current_player.deck.pop())
    else:
        current_player.health -= 1
    return game_state_cpy

#######
# Actions called by player
#######


def play_spell(player_name, card_idx, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    card_to_use = current_player.cards[card_idx]
    current_player.already_used_mana += card_to_use.cost
    game_state_cpy = card_to_use.apply(game_state_cpy, current_player, None)
    return game_state_cpy


def put_minion(player_name, card_idx, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    card = current_player.cards[card_idx]
    current_player.minions.append(card)
    current_player.cards.remove(card)
    return game_state_cpy


def play_minion(player_name, minion_idx, target, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    minion_to_use = current_player.minions[minion_idx]
    current_player.already_used_mana += minion_to_use.cost
    game_state_cpy = current_player.minions[minion_idx]\
        .apply(game_state_cpy, current_player, target)
    return game_state_cpy



