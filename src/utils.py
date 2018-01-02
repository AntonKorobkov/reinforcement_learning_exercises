
import matplotlib.pyplot as plt
import numpy as np


# нужно добавить сюда ещё возможность подписывать оси
def plot_multiple_results(figures, labels, start=0, stop=6000, iterations=500):

    stepnum = stop/iterations

    space = np.arange(start, stop, stepnum)

    for fignum, fig in enumerate(figures):
        plt.plot(space, fig, label=labels[fignum])

    plt.legend(loc='best')
    plt.show()

