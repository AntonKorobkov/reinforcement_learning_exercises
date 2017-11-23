"""
determine the choice of arm to
"""

import matplotlib.pyplot as plt

class Strategy:
    """
    when we pull the lever
    we implement some sort of choice that we sustain
    over
    """

    def __init__(self, bandit, iterations):
        """
        reward is being updated while iterating
        """
        self.reward_list = []
        self.bandit = bandit
        self.iterations = iterations

        # the key will be lever number, value - number of attempts and mean value
        self.lever_rewards = {}

    def update_reward_list(self, value):

        try:
            self.reward_list.append([len(self.reward_list), self.reward_list[len(self.reward_list) - 1][1] + value])
        except IndexError:
            self.reward_list.append([0, value])

    @property
    def reward_array(self):
        return [i[1] for i in self.reward_list]


class GreedyStrategy(Strategy):
    """
    when we pull the lever
    we implement some sort of choice that we sustain
    over multiple iterations according to our strategy
    """

    def __call__(self, *args, **kwargs):
        if kwargs.get('learn_sample_size'):
            self.launch_strategy(kwargs.get('learn_sample_size'))
        else:
            self.launch_strategy()

    def launch_strategy(self, learn_sample_size=3):
        """
        how do we choose lever to pull
        for each lever we perform learning attempts
        then we choose the lever with highest average result
        """
        highest_value_arm, best_levnum = 0, None

        for lev in range(self.bandit.arms):
            total_value_training = 0

            for i in range(learn_sample_size):
                pull_result = self.bandit.pull_lever(lev)

                total_value_training += pull_result
                self.update_reward_list(pull_result)
                self.iterations -= 1

                if self.iterations == 0:
                    break

            if total_value_training > highest_value_arm:
                best_levnum = lev
                highest_value_arm = total_value_training

        if self.iterations > 0:
            for i in range(self.iterations):
                self.update_reward_list(self.bandit.pull_lever(best_levnum))
