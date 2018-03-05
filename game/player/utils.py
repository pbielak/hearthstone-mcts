"""Utils"""


def can_use_card(player, card, game_state):
    current_player, _ = get_players(game_state, player)
    return current_player.already_used_mana + card.cost <= current_player.mana


def can_put_minion(player, game_state, cfg):
    current_player, _ = get_players(game_state, player)
    return len(current_player.minions) < cfg.MAX_MINIONS


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
