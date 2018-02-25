from game.config import load_cfg
from game.engine import GameEngine


def main():
    cfg = load_cfg()
    engine = GameEngine(cfg)
    engine.run()


if __name__ == '__main__':
    main()
