"""
Module for running the random simulations (playouts)
"""
from game import engine
from game.player import agent
from game.player import utils
from game import state


def simulate_random_game(game_state):
    """
    Runs game till end using two random agent players
    and returns which player won.

    :param game_state: (GameState) current state of the game
    :return: +1 if current player won, -1 if current player lost
    """
    if game_state.is_terminal():
        winning_player = game_state.get_winning_player()
        current_player, _ = game_state.get_players()
    else:
        game_state_sim = prepare_simulation_game_state(game_state)
        current_player, _ = game_state_sim.get_players()

        eng = engine.GameEngine(game_state_sim)
        winning_player = eng.run()

    if winning_player.name == current_player.name:
        return 1

    return -1


def prepare_simulation_game_state(game_state):
    ra_A = utils.create_player_from_another_player(
        target_player_cls=agent.RandomAgent,
        source_player_obj=game_state.player_A
    )

    ra_B = utils.create_player_from_another_player(
        target_player_cls=agent.RandomAgent,
        source_player_obj=game_state.player_B
    )

    curr_step = game_state.curr_step

    return state.GameState(player_A=ra_A,
                           player_B=ra_B,
                           curr_step=curr_step)
