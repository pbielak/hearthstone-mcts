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
    if player_name == game_state_cpy.player_A.name:
        game_state_cpy.player_A.cards.append(game_state_cpy.player_A.deck.pop())  # change to card here and below :)
    elif player_name == game_state_cpy.player_B.name:
        game_state_cpy.player_B.cards.append(game_state_cpy.player_A.deck.pop())
    else:
        raise ValueError("Wrong player!")
    return game_state_cpy
