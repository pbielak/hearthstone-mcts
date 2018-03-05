"""Utils"""
from game import action
from game.cards.card import MinionCard, SpellCard


def can_use_card(player, card):
    return player.already_used_mana + card.cost <= player.mana


def can_put_minion(player, cfg):
    return len(player.minions) < cfg.MAX_MINIONS


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


def get_possible_actions(game_state, player, cfg):
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
        if isinstance(card, SpellCard):
            actions['spell_plays'].append(
                (action.play_spell, (player, idx, game_state))
            )
        # Put minion cards
        elif isinstance(card, MinionCard):
            if not can_put_minion(player, cfg):
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
