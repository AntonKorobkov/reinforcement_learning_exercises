
import matplotlib.pyplot as plt
import numpy as np


def plot_multiple_results(figures, start=0, stop=6000, iterations=500):

    stepnum = stop/iterations

    space = np.arange(start, stop, stepnum)

    for fig in figures:
        plt.plot(space, fig)

    plt.show()

