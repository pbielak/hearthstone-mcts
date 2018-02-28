"""Prints current game state"""


def prepare_state(game_state, cfg):
    # TODO: add actions list
    # Which action?
    # 0. Take card
    # 1. Put minion on field (which one?)
    # 2. Call spell card (which one?)
    # 3. Attack with minion (which one? whom?)

    game_state_str = "\n" \
                     "Player B {player_B_name} (Health: " \
                     "{player_B_health}/{total_health})\n" \
                     "Cards: {player_B_cards}\n" \
                     "Minions: {player_B_minions}\n" \
                     "==============================\n" \
                     "Minions: {player_A_minions}\n" \
                     "Cards: {player_A_cards}\n" \
                     "Player A {player_A_name} (Health: " \
                     "{player_A_health}/{total_health})\n" \
                     "\n"

    game_state_str = game_state_str.format(
        player_B_name=game_state.player_B.name,
        player_B_health=game_state.player_B.health,
        player_B_cards=game_state.player_B.cards,
        player_B_minions=game_state.player_B.minions,
        player_A_minions=game_state.player_A.minions,
        player_A_cards=game_state.player_A.cards,
        player_A_name=game_state.player_A.name,
        player_A_health=game_state.player_A.health,
        total_health=cfg.INITIAL_HEALTH
    )

    return game_state_str
