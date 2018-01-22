import argparse

from bandit import NormalBandit
from strategy import GreedyStrategy, EpsilonGreedyStrategy
from utils import plot_multiple_results


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Provide number of iterations and number of arms')
    parser.add_argument('--arms', type=int, help='This many arms bandit should have', default=50)
    parser.add_argument('--iterations', type=int, help='This many iterations will be launched', default=1000)
    parser.add_argument('--epsilon_greedy', type=float, help='This is epsilon for greedy strategy', default=0.01)
    parser.add_argument('--learn_sample_size', type=int, default=15)
    parser.add_argument('--max_switches', type=int, default=2)
    parser.add_argument('--normal_distribution_mean', type=int, default=6)
    parser.add_argument('--normal_distribution_deviation', type=int, default=2)
    parser.add_argument('--best_arm_ratio', type=float, default=0.1)
    args = parser.parse_args()

    bandit = NormalBandit(int(args.arms), average=args.normal_distribution_mean, std=args.normal_distribution_deviation)

    # TODO: switch between different bandits when implemented
    test_strategy = GreedyStrategy(bandit, int(args.iterations))
    epsilon_strategy = EpsilonGreedyStrategy(bandit, int(args.iterations))
    test_strategy(learn_sample_size=args.learn_sample_size)
    epsilon_strategy(learn_sample_size=args.learn_sample_size, epsilon=args.epsilon_greedy,
                     max_switches=args.max_switches, best_levs_rat=args.best_arm_ratio)
    labels_array = ['Greedy strategy', 'Epsilon greedy strategy']

    plot_multiple_results([test_strategy.reward_array, epsilon_strategy.reward_array], labels_array,
                          iterations=args.iterations)


