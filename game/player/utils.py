"""Utils"""
from game import action
from game import config
from game.cards import card as cards


def can_use_card(player, card):
    return player.already_used_mana + card.cost <= player.mana


def can_put_minion(player):
    return len(player.minions) < config.MAX_MINIONS


def cleanup_all_dead_minions(game_state):
    for player in (game_state.player_A, game_state.player_B):
        player.minions = [
            minion for minion in player.minions if minion.health > 0
        ]


def get_players(game_state, source):
    if source is game_state.player_A:
        player, opponent = game_state.player_A, game_state.player_B
    elif source is game_state.player_B:
        player, opponent = game_state.player_B, game_state.player_A
    else:
        raise ValueError('Source must be a player!')

    return player, opponent


def get_possible_actions(game_state, player):
    actions = {
        'spell_plays': [],
        'minion_puts': [],
        'minion_plays': [],
        'no_actions': None
    }

    _, opponent = get_players(game_state, player)

    for idx, card in enumerate(player.cards):
        if not can_use_card(player, card):
            continue

        # Play spell cards
        if isinstance(card, cards.SpellCard):
            actions['spell_plays'].append(
                (action.play_spell, (player, idx, game_state))
            )
        # Put minion cards
        elif isinstance(card, cards.MinionCard):
            if not can_put_minion(player):
                continue
            actions['minion_puts'].append(
                (action.put_minion, (player, idx))
            )

    # Play minion (attack)
    for idx, minion in enumerate(player.minions):
        if not minion.can_attack:
            continue

        for target in (opponent, *opponent.minions):
            actions['minion_plays'].append(
                (action.play_minion, (player, idx, target, game_state))
            )

    actions['no_actions'] = (not actions['spell_plays']) and \
                            (not actions['minion_plays']) and \
                            (not actions['minion_puts'])

    return actions
