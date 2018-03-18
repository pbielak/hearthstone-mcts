from game.config import load_cfg
from game.engine import GameEngine


def main():
    cfg = load_cfg()
    engine = GameEngine(cfg)
    engine.run()


if __name__ == '__main__':
    main()


# Zdefiniowanie gracza agresywnego, defensywnego
# Badanie wydajności (wykresy, czas -> głębokość węzła, średniego węzła itp.)
# Przynajmniej 100 gier (połowa pierwszy gracz MC, połowę drugi gracz MC)
# 100 x 3 agentów (drugi gracz)
