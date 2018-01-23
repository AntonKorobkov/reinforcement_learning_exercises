"""
My n-armed bandit implementation
for now only noraml distribution with hardcoded params
"""
from random import randint
from numpy.random import normal


class Bandit:

    def __init__(self, arms, **kwargs):
        self.arms = arms
        self.parameters = {}
        self.set_parameters(**kwargs)

    def set_parameters(self, kwargs):
        """
        set parameters according to chosen distribution
        """

    def pull_lever(self, armnumber):
        """
        pull the lever by lever number
        """


class NormalBandit(Bandit):

    def set_parameters(self, **kwargs):
        for i in range(self.arms):
            # set mean and deviation
            random_average = kwargs.get('average') + randint(-int((kwargs.get('average') / 20) * 100),
                                                             (int(kwargs.get('average') / 20) * 100)) / 100

            self.parameters.update({i: {'average': random_average, 'std': kwargs.get('std')}})

    def pull_lever(self, armnumber):
        return normal(self.parameters[armnumber]['average'], self.parameters[armnumber]['std'])
