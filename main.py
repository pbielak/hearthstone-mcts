from game import action
from game import config
from game import engine
from game.player import utils
from game import state

from mcts.simulation import simulate_random_game


def create_initial_game_state():
    player_A = utils.create_player_from_default_config(
        config.PLAYER_A_CLS, 'Pyjter'
    )
    player_B = utils.create_player_from_default_config(
        config.PLAYER_B_CLS, 'Mati'
    )
    curr_step = 0

    return state.GameState(player_A, player_B, curr_step)


def prepare_game(game_state):
    for _ in range(3):
        action.take_card(game_state.player_A)

    for _ in range(4):
        action.take_card(game_state.player_B)


def main_normal_game():
    gs = create_initial_game_state()
    prepare_game(gs)

    eng = engine.GameEngine(gs)
    eng.run()


def main():
    # results = []
    #
    # for i in range(1000):
    #     print(i)
    #     gs = create_initial_game_state()
    #     prepare_game(gs)
    #
    #     sim_result = simulate_random_game(gs)
    #     results.append(sim_result)
    #
    # from collections import Counter
    # cnt_results = Counter(results)
    # print('#Wins:', cnt_results[1])
    # print('#Looses:', cnt_results[-1])
    from copy import deepcopy
    from mcts.turn import generate_all_turns

    gs = create_initial_game_state()
    prepare_game(gs)

    turns = generate_all_turns(deepcopy(gs))
    print(turns)


if __name__ == '__main__':
    main_normal_game()
    # main()


# Zdefiniowanie gracza agresywnego, defensywnego
# Badanie wydajności (wykresy, czas -> głębokość węzła, średniego węzła itp.)
# Przynajmniej 100 gier (połowa pierwszy gracz MC, połowę drugi gracz MC)
# 100 x 3 agentów (drugi gracz)
