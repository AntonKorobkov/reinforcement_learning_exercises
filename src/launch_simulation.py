import argparse

from bandit import NormalBandit
from strategy import GreedyStrategy, EpsilonGreedyStrategy
from utils import plot_multiple_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provide number of iterations and number of arms')
    parser.add_argument('--arms', type=int, help='This many arms bandit should have', default=50)
    parser.add_argument('--iterations', type=int, help='This many iterations will be launched', default=1000)
    args = parser.parse_args()

    bandit = NormalBandit(int(args.arms), average=6, std=2)

    test_strategy = GreedyStrategy(bandit, int(args.iterations))
    epsilon_strategy = EpsilonGreedyStrategy(bandit, int(args.iterations))
    test_strategy(learn_sample_size=15)
    epsilon_strategy(learn_sample_size=15, epsilon=0.01)
    labels_array = ['Greedy strategy', 'Epsilon greedy strategy']

    plot_multiple_results([test_strategy.reward_array, epsilon_strategy.reward_array], labels_array,
                          iterations=args.iterations)

