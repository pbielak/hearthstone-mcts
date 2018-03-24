"""
Analysis (graph maker script)
"""
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PlotConfig = namedtuple('PlotConfig', ['filepath', 'title', 'output_filename',
                                       'time_interval'])


def get_plot_configs():
    plots = [
        PlotConfig('data/MCTS_RA/stats_MCTSPlayer_RandomAgent_1.txt',
                   'MCTS vs Agent Losowy - Przegrane (30%)',
                   'MCTS_RA_LOST.png', 30),

        PlotConfig('data/MCTS_RA/stats_MCTSPlayer_RandomAgent_3.txt',
                   'MCTS vs Agent Losowy - Wygrane (70%)',
                   'MCTS_RA_WIN.png', 30),

        PlotConfig('data/RA_MCTS/stats_RandomAgent_MCTSPlayer_1.txt',
                   'Agent Losowy vs MCTS - Przegrane (50%)',
                   'RA_MCTS_LOST.png', 30),

        PlotConfig('data/RA_MCTS/stats_RandomAgent_MCTSPlayer_3.txt',
                   'Agent Losowy vs MCTS - Wygrane (50%)',
                   'RA_MCTS_WIN.png', 30),

        PlotConfig('data/MCTS_AA/stats_MCTSPlayer_AggressiveAgent_1.txt',
                   'MCTS vs Agent Agresywny - Przegrane (90%)',
                   'MCTS_AA_LOST.png', 60),

        PlotConfig('data/MCTS_AA/stats_MCTSPlayer_AggressiveAgent_7.txt',
                   'MCTS vs Agent Agresywny - Wygrane (10%)',
                   'MCTS_AA_WIN.png', 60),

        PlotConfig('data/AA_MCTS/stats_AggressiveAgent_MCTSPlayer_10.txt',
                   'Agent Agresywny vs MCTS - Przegrane (100%)',
                   'AA_MCTS_LOST.png', 60),

        PlotConfig('data/MCTS_CA/stats_MCTSPlayer_ControllingAgent_9.txt',
                   'MCTS vs Agent Kontrolujący - Przegrane (20%)',
                   'MCTS_CA_LOST.png', 60),

        PlotConfig('data/MCTS_CA/stats_MCTSPlayer_ControllingAgent_5.txt',
                   'MCTS vs Agent Kontrolujący - Wygrane (80%)',
                   'MCTS_CA_WIN.png', 60),

        PlotConfig('data/CA_MCTS/stats_ControllingAgent_MCTSPlayer_9.txt',
                   'Agent Kontrolujący vs MCTS - Wygrane (100%)',
                   'CA_MCTS_WIN.png', 60)
    ]

    return plots


def get_split_idxs(df):
    split_points = []

    nb_simulations = df['nb_simulations'].values
    for idx in range(len(df) - 1):
        if nb_simulations[idx] > nb_simulations[idx + 1]:
            split_points.append(idx + 1)

    return split_points


def draw_plot(x, y, x_lines, ylabel, label, subplot, color):
    line, = subplot.plot(x, y, marker='.', markersize=1, linestyle='',
                         label=label, color=color)

    for sp_idx in x_lines:
        subplot.axvline(x=x[sp_idx], color='0.1', linestyle='--')

    subplot.set_ylabel(ylabel)
    return line


def timestamps_to_relative_time(df):
    timestamps = df['#timestamp'].values
    time = []

    base_ts = timestamps[0]
    for idx, ts in enumerate(timestamps):
        time.append(timestamps[idx] - base_ts)

    return time


def main():

    for plot_cfg in get_plot_configs():
        print('Plotting', plot_cfg.title)

        fig, subplots = plt.subplots(3, 1, sharex=True, figsize=(15, 8))

        df = pd.read_csv(plot_cfg.filepath, sep=';')

        time = timestamps_to_relative_time(df)
        x_lines = get_split_idxs(df)

        nb_simulations = df['nb_simulations'].values.tolist()

        l1 = draw_plot(x=time, y=nb_simulations, x_lines=x_lines,
                       ylabel='Liczba symulacji', subplot=subplots[0],
                       label='Łączna liczba symulacji', color='blue')

        avg_children = df['avg_children'].values.tolist()

        l2 = draw_plot(x=time, y=avg_children, x_lines=x_lines,
                       ylabel='% dzieci', subplot=subplots[1],
                       label='Średni procent odwiedzonych dzieci',
                       color='darkgreen')

        max_depth = df['max_depth'].values.tolist()
        avg_depth = df['avg_depth'].values.tolist()
        median_depth = df['median_depth'].values.tolist()

        l3 = draw_plot(x=time, y=max_depth, x_lines=x_lines,
                       ylabel='Głębokość liści', subplot=subplots[2],
                       label='Max. głębokość', color='red')

        l4 = draw_plot(x=time, y=avg_depth, x_lines=x_lines,
                       ylabel='Głębokość liści', subplot=subplots[2],
                       label='Średnia głębokość', color='orange')

        l5 = draw_plot(x=time, y=median_depth, x_lines=x_lines,
                       ylabel='Głębokość liści', subplot=subplots[2],
                       label='Mediana głębokości', color='indigo')

        subplots[0].set_yscale('log')
        subplots[1].set_ylim((0, 100))

        plt.xlabel('Czas [s]')
        plt.xlim((0, time[-1]))
        plt.xticks(np.arange(0, time[-1], plot_cfg.time_interval))

        plt.suptitle(plot_cfg.title +
                     ' [Łączny czas: {} (s)]'.format(int(time[-1])))

        legend = plt.figlegend((l1, l2, l3, l4, l5),
                      ('Łączna liczba symulacji',
                       'Średni procent odwiedzonych dzieci',
                       'Max. głębokość', 'Średnia głębokość',
                       'Mediana głębokości'),
                      'right', bbox_to_anchor=(1.00, 0.91))

        for legend_handle in legend.legendHandles:
            legend_handle._legmarker.set_markersize(9)

        plt.savefig('plots/' + plot_cfg.output_filename)
    # plt.show()


def make_fig_latex():
    import os
    plots = []

    for f in os.listdir('plots'):
        if os.path.isfile(os.path.join('plots', f)):
            plots.append(os.path.join('imgs/plots', f))

    print(plots)

    for p in plots:
        fig_str = """
    \\begin{figure}[H]
        \\center
        \\includegraphics[width=\\textwidth]{%s}
    \\end{figure}
            """ % p
        print(fig_str)


if __name__ == '__main__':
    main()
