def get_card_to_use(pocket, clazz, action):
    card_type = clazz.__name__
    info_fmt_str = "Available {card_type}s:".format(
        card_type=card_type)
    action_fmt_str = "Choose {card_type} to {action}:".format(
        card_type=card_type, action=action)
    print(info_fmt_str)

    for card_idx, card in enumerate(pocket):
        if isinstance(card, clazz):
            print(card_idx, "=>", card)

    # TODO: return correct idx (check input string,
    # maybe can be something other than number)
    choice = int(input(action_fmt_str))
    if type(pocket[choice]).__name__ == clazz.__name__:
        return choice
    else:
        raise ValueError("Not correct card index...")


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
