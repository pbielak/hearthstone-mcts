"""Player action"""
from game import config

# Single action like:
#     * take card from deck (always forced; if no cards in deck,
#                            loose health points)
#     * play minion card (attack; against whom?)
#     * play spell card
#     * put minion on field (max. 7 on field)

#######
# Actions called by system
#######


def increment_mana(player):
    if player.mana < config.MAX_MANA:
        player.mana += 1


def take_card(player):
    if not player.deck.is_empty():
        player.cards.append(player.deck.pop())
    else:
        player.deck.no_attempt_pop_when_empty += 1
        player.health -= player.deck.no_attempt_pop_when_empty

#######
# Actions called by player
#######


def play_spell(card_idx, game_state):
    player, _ = game_state.get_players()

    card = player.cards[card_idx]
    player.already_used_mana += card.cost
    card.apply(game_state, player, None)
    player.cards.remove(card)


def put_minion(card_idx, game_state):
    player, _ = game_state.get_players()

    minion = player.cards[card_idx]
    minion.can_attack = False
    player.minions.append(minion)
    player.cards.remove(minion)
    player.already_used_mana += minion.cost


def play_minion(minion_idx, target_idx, game_state):
    player, opponent = game_state.get_players()

    if target_idx == -1:
        target = opponent
    else:
        target = opponent.minions[target_idx]

    minion = player.minions[minion_idx]
    minion.apply(game_state, player, target)
    minion.can_attack = False
