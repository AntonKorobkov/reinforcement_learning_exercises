"""
My n-armed bandit implementation
for now only noraml distribution with hardcoded params
"""
from random import randint
from numpy.random import normal


class Bandit:

    def __init__(self, arms):
        self.arms = arms
        self.parameters = []
        self.set_parameters()

    def set_parameters(self):
        """
        set parameters according to chosen distribution
        """

    def pull_lever(self, armnumber):
        """
        pull the lever by number
        """


class NormalBandit(Bandit):

    def set_parameters(self):
        for i in range(self.arms):
            # set mean and deviation
            self.parameters.append((randint(0, 10), randint(2, 4)))

    def pull_lever(self, armnumber):
        # дернуть за руку
        return normal(self.parameters[armnumber][0], self.parameters[armnumber][1])
