from game import action
from game import config
from game import engine
from game.player import utils
from game import state
from mcts import stats


def create_initial_game_state():
    player_A = utils.create_player_from_default_config(
        config.PLAYER_A_CLS, 'PLAYER_A'
    )
    player_B = utils.create_player_from_default_config(
        config.PLAYER_B_CLS, 'MCTSPlayer'
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
    winning_player = eng.run()
    print(winning_player.__class__.__name__, 'won the game!')


def main():
    for i in range(10):
        stats.instance = stats.StatsCounter(
            filename='stats_{}_{}_{}.txt'.format(
                config.PLAYER_A_CLS.__name__, config.PLAYER_B_CLS.__name__, i + 1
            )
        )
        try:
            main_normal_game()
        except:
            print('Exception occurred')
            continue


if __name__ == '__main__':
    # main_normal_game()
    main()


# Zdefiniowanie gracza agresywnego, defensywnego
# Badanie wydajności (wykresy, czas -> głębokość węzła, średniego węzła itp.)
# Przynajmniej 100 gier (połowa pierwszy gracz MC, połowę drugi gracz MC)
# 100 x 3 agentów (drugi gracz)
