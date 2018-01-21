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
            self.parameters['average'] = kwargs.get('average')
            self.parameters['std'] = kwargs.get('std')

    def pull_lever(self, armnumber):
        return normal(self.parameters['average'], self.parameters['std'])
