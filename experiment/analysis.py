"""
Analysis (graph maker script)
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main():
    plots = [
        ('MCTS_RA/stats_MCTSPlayer_RandomAgent_1.txt', 5500, 50, 'MCTS vs RandomAgent - Lost (30%)', 'MCTS_RA_LOST.png'),
        ('MCTS_RA/stats_MCTSPlayer_RandomAgent_3.txt', 4000, 50, 'MCTS vs RandomAgent - Won (70%)', 'MCTS_RA_WIN.png'),

        ('RA_MCTS/stats_RandomAgent_MCTSPlayer_1.txt', 2500, 50, 'RandomAgent vs MCTS - Lost (50%)', 'RA_MCTS_LOST.png'),
        ('RA_MCTS/stats_RandomAgent_MCTSPlayer_3.txt', 3300, 50, 'RandomAgent vs MCTS - Won (50%)', 'RA_MCTS_WIN.png'),


        ('MCTS_AA/stats_MCTSPlayer_AggressiveAgent_1.txt', 5000, 50, 'MCTS vs AggressiveAgent - Lost (90%)', 'MCTS_AA_LOST.png'),
        ('MCTS_AA/stats_MCTSPlayer_AggressiveAgent_7.txt', 7500, 50, 'MCTS vs AggressiveAgent - Won (10%)', 'MCTS_AA_WIN.png'),

        ('AA_MCTS/stats_AggressiveAgent_MCTSPlayer_10.txt', 9500, 50, 'AggresiveAgent vs MCTS - Lost (100%)', 'AA_MCTS_LOST.png'),

        ('MCTS_CA/stats_MCTSPlayer_ControllingAgent_9.txt', 8500, 50, 'MCTS vs ControllingAgent - Lost (20%)', 'MCTS_CA_LOST.png'),
        ('MCTS_CA/stats_MCTSPlayer_ControllingAgent_5.txt', 17500, 50, 'MCTS vs ControllingAgent - Won (80%)', 'MCTS_CA_WIN.png'),

        ('CA_MCTS/stats_ControllingAgent_MCTSPlayer_9.txt', 20000, 100, 'ControllingAgent vs MCTS - Won (100%)', 'CA_MCTS_WIN.png')
    ]

    for plot_cfg in plots:
        print('Plotting', plot_cfg[3])
        plt.figure()
        df = pd.read_csv(plot_cfg[0], sep=';')

        exec_time = df['#timestamp'].values[-1] - df['#timestamp'].values[0]
        exec_time = round(exec_time)
        del df['#timestamp']

        for column in df.columns.values:
            data = df[column].values
            plt.plot(data, label=column)

        plt.xlim((0, plot_cfg[1]))
        plt.ylim((0, plot_cfg[2]))
        plt.title(plot_cfg[3] + ' [Time: {} (s)]'.format(int(exec_time)))
        plt.tight_layout()
        plt.legend()

        plt.savefig('plots/' + plot_cfg[4])
    #plt.show()


if __name__ == '__main__':
    main()
