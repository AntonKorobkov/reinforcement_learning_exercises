"""
determine the choice of arm to
"""

from random import randint
from queue import PriorityQueue
from math import ceil

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


class StrategyLaunch(Strategy):

    def __call__(self, *args, **kwargs):
        self.launch_strategy(**kwargs)

    def launch_strategy(self, **kwargs):
        pass


class GreedyStrategy(StrategyLaunch):
    """
    when we pull the lever
    we implement some sort of choice that we sustain
    over multiple iterations according to our strategy
    """

    def __call__(self, *args, **kwargs):
        self.launch_strategy(**kwargs)


    def launch_strategy(self, **kwargs):
        """
        how do we choose lever to pull
        for each lever we perform learning attempts
        then we choose the lever with highest average result
        """
        highest_value_arm, best_levnum = 0, None

        for lev in range(self.bandit.arms):
            total_value_training = 0

            for i in range(kwargs.get('learn_sample_size')):
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


class EpsilonGreedyStrategy(StrategyLaunch):
    """
    We sustain a choice but we also check alternatives once in a while
    """

    def launch_strategy(self, **kwargs):
        """
        how do we choose lever to pull
        for each lever we perform learning attempts
        then we choose the lever with highest average result
        what if we set a limit to the number of switches.

        """

        switches = 0

        highest_value_arm, best_levnum, avg_arm_dict = 0, None, {}

        lev_queue = PriorityQueue(maxsize=ceil(kwargs.get('best_levs_rat') * self.bandit.arms))

        for lev in range(self.bandit.arms):
            total_value_training, iterations_performed = 0, 0

            for i in range(kwargs.get('learn_sample_size')):
                pull_result = self.bandit.pull_lever(lev)

                if not avg_arm_dict.get(lev):
                    avg_arm_dict[lev] = [pull_result, 1]
                else:
                    self.update_average_values_dict(avg_arm_dict, pull_result, lev)

                total_value_training += pull_result
                self.update_reward_list(pull_result)
                self.iterations -= 1
                iterations_performed += 1

                if self.iterations == 0:
                    break

                average_trained = total_value_training / iterations_performed

            if total_value_training > highest_value_arm:
                best_levnum = lev
                highest_value_arm = total_value_training
                average_highest = average_trained

            if lev_queue.full() is not True:
                lev_queue.put((average_trained, lev))
            else:
                minval = lev_queue.get()

                if minval[0] < average_trained:
                    lev_queue.put((average_trained, lev))
                else:
                    lev_queue.put(minval)

        if self.iterations > 0:

            best_levnums = [i[1] for i in lev_queue.queue]
            current_best_index = best_levnums.index(best_levnum)

            for i in range(self.iterations):

                if randint(1, 100) > kwargs.get('epsilon') * 100 or switches >= kwargs.get('max_switches'):
                    chosen_lever_pull = self.bandit.pull_lever(best_levnum)
                    self.update_reward_list(chosen_lever_pull)
                    self.update_average_values_dict(avg_arm_dict, chosen_lever_pull, best_levnum)

                else:

                    random_lever = randint(0, len(best_levnums) - 1)
                    if random_lever == current_best_index:
                        while random_lever == current_best_index:
                            random_lever = randint(0, len(best_levnums) - 1)


                    random_pull_result = self.bandit.pull_lever(best_levnums[random_lever])
                    self.update_reward_list(random_pull_result)
                    self.update_average_values_dict(avg_arm_dict, random_pull_result, best_levnums[random_lever])

                    if avg_arm_dict[best_levnums[random_lever]][0] > average_highest:

                        average_highest = avg_arm_dict[best_levnums[random_lever]][0]
                        best_levnum = best_levnums[random_lever]
                        switches += 1
                        current_best_index = random_lever

    def update_average_values_dict(self, avgvdict, value, elnum):

        next_step = avgvdict[elnum][1] + 1

        avgvdict[elnum] = [(avgvdict[elnum][0] * (next_step - 1) +
                            value) / next_step, next_step]
