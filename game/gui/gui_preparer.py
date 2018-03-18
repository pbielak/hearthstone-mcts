"""Prints current game state"""
from game import config


def prepare_state(game_state):

    game_state_str = "\n" \
                     "Player B {player_B_name} (mana: " \
                     "{player_B_used_mana}/{player_B_total_mana}, " \
                     "health: {player_B_health}/{total_health})\n" \
                     "Cards: {player_B_cards}\n" \
                     "Minions: {player_B_minions}\n" \
                     "==============================\n" \
                     "Minions: {player_A_minions}\n" \
                     "Cards: {player_A_cards}\n" \
                     "Player A {player_A_name} (mana: " \
                     "{player_A_used_mana}/{player_A_total_mana}, " \
                     "health: {player_A_health}/{total_health})\n" \
                     "\n"

    game_state_str = game_state_str.format(
        player_B_name=game_state.player_B.name,
        player_B_health=game_state.player_B.health,
        player_B_used_mana=game_state.player_B.already_used_mana,
        player_B_total_mana=game_state.player_B.mana,
        player_B_cards=_make_card_list(game_state.player_B.cards),
        player_B_minions=_make_card_list(game_state.player_B.minions),

        player_A_name=game_state.player_A.name,
        player_A_health=game_state.player_A.health,
        player_A_used_mana=game_state.player_A.already_used_mana,
        player_A_total_mana=game_state.player_A.mana,
        player_A_cards=_make_card_list(game_state.player_A.cards),
        player_A_minions=_make_card_list(game_state.player_A.minions),

        total_health=config.INITIAL_HEALTH
    )

    return game_state_str


def _make_card_list(cards):
    cards_str = [str(card) for card in cards]

    # return "[\n{}\n]".format('\n'.join(cards_str))
    return "{}".format(cards)
