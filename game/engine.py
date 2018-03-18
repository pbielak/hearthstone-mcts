"""Game engine"""
from copy import deepcopy

from game import action
from game import config
from game.player import utils
from game import state


class GameEngine(object):
    """Object implementing main loop / logic of game

    Attributes:
        * game_state (GameState): the current game state
    """
    def __init__(self):
        self.game_state = create_initial_game_state()
        prepare_game(self.game_state)

    def run(self):
        while not self.game_state.is_terminal_state():
            self.game_state.curr_step += 1
            game_state_cpy = deepcopy(self.game_state)

            player = choose_player(game_state_cpy)
            game_state_cpy = prepare_player(player, game_state_cpy)
            player.play_turn(game_state_cpy)

            self.game_state = game_state_cpy

        winning_player = self.game_state.get_winning_player()
        print('Player {} won the game!'.format(winning_player.name))


def create_initial_game_state():
    player_A = utils.create_player_from_default_config(
        config.PLAYER_A_CLS, 'Pyjter'
    )
    player_B = utils.create_player_from_default_config(
        config.PLAYER_B_CLS, 'Mati'
    )
    curr_step = 0

    return state.GameState(player_A, player_B, curr_step)


def choose_player(game_state):
    if game_state.curr_step % 2 == 1:
        return game_state.player_A
    return game_state.player_B


def prepare_player(player, game_state):
    action.take_card(player)
    action.increment_mana(player)
    player.already_used_mana = 0

    for minion in player.minions:
        minion.can_attack = True

        if minion.side_effect is not None:
            minion.side_effect(game_state, player, None)

    return game_state


def prepare_game(game_state):
    for _ in range(3):
        action.take_card(game_state.player_A)

    for _ in range(4):
        action.take_card(game_state.player_B)
