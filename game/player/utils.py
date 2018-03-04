"""Utils"""


def get_card_to_use(cards_list, cls):
    info_fmt_str = "Available {card_type}s:".format(card_type=cls.__name__)
    action_fmt_str = "Choose one card:"
    print(info_fmt_str)

    for card_idx, card in enumerate(cards_list):
        if isinstance(card, cls):
            print(card_idx, "=>", card)

    choice = int(input(action_fmt_str))
    if isinstance(cards_list[choice], cls):
        return choice
    else:
        raise ValueError("Incorrect card index...")


def can_use_card(player_name, card, game_state):
    current_player = get_current_player(player_name, game_state)
    return current_player.already_used_mana + card.cost <= current_player.mana


def can_put_minion(player_name, game_state, cfg):
    current_player = get_current_player(player_name, game_state)
    return len(current_player.minions) < cfg.MAX_MINIONS


def get_current_player(player_name, game_state):
    if player_name == game_state.player_A.name:
        return game_state.player_A
    elif player_name == game_state.player_B.name:
        return game_state.player_B
    else:
        raise ValueError("Wrong player!")


def cleanup_all_dead_minions(game_state):
    for player in (game_state.player_A, game_state.player_B):
        player.minions = [
            minion for minion in player.minions if minion.health > 0
        ]
