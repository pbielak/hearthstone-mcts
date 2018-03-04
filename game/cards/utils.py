"""Utils"""


def get_players(game_state, source):
    if source is game_state.player_A:
        player, opponent = game_state.player_A, game_state.player_B
    elif source is game_state.player_B:
        player, opponent = game_state.player_B, game_state.player_A
    else:
        raise ValueError('Source must be a player!')

    return player, opponent
