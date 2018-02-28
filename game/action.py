"""Player action"""
from copy import deepcopy

# Single action like:
#     * take card from deck (always forced; if no cards in deck,
#                            loose health points)
#     * play minion card (attack; against whom?)
#     * play curse / magic card
#     * put minion on field (max. 7 on field)


def take_card(player_name, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    current_player.cards.append(current_player.deck.pop())
    return game_state_cpy


def play_spell(player_name, card_idx, game_state):
    game_state_cpy = deepcopy(game_state)
    current_player = get_current_player(player_name, game_state_cpy)
    game_state_cpy = current_player.cards[card_idx].apply(game_state_cpy,
                                                          current_player, None)
    return game_state_cpy


def get_current_player(player_name, game_state):
    if player_name == game_state.player_A.name:
        return game_state.player_A
    elif player_name == game_state.player_B.name:
        return game_state.player_B
    else:
        raise ValueError("Wrong player!")
