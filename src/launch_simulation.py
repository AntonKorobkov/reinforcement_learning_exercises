import argparse

from bandit import NormalBandit
from strategy import GreedyStrategy
from utils import plot_multiple_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provide number of iterations and number of arms')
    parser.add_argument('--arms', type=int, help='This many arms bandit should have', default=10)
    parser.add_argument('--iterations', type=int, help='This many iterations will be launched', default=500)
    args = parser.parse_args()

    bandit = NormalBandit(int(args.arms))

    test_strategy = GreedyStrategy(bandit, int(args.iterations))
    test_strategy()
    plot_multiple_results([test_strategy.reward_array], iterations=args.iterations)

