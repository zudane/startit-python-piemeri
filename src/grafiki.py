import matplotlib.pyplot as plt
import numpy as np


def linijas():
    ypoints = np.array(np.random.randint(100, size=(10)))
    ypoints2 = np.array(np.random.randint(100, size=(10)))

    plt.plot(ypoints, 'o-.')
    plt.plot(ypoints2, '+:r')
    plt.show()


def punkti():
    x = np.array(np.random.randint(20, size=(30)))
    y = np.array(np.random.randint(100, size=(30)))
    plt.scatter(x, y)
    plt.show()


def stabini():
    x = np.array(["A", "B", "C", "D"])
    y = np.array([3, 8, 1, 10])

    plt.bar(x,y)
    plt.show()


def rinka():
    y = np.array([35, 25, 25, 15])
    mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

    plt.pie(y, labels = mylabels)
    plt.show()


def histogramma():
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    x = mu + sigma * np.random.randn(437)

    num_bins = 50

    fig, ax = plt.subplots()

    # histogramma
    n, bins, patches = ax.hist(x, num_bins, density=True)

    # līnija
    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
        np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    ax.plot(bins, y, '--')
    ax.set_xlabel('Dati')
    ax.set_ylabel('Varbūtība')
    ax.set_title(r'Nejaušu datu histogramma: $\mu=100$, $\sigma=15$')

    fig.tight_layout()
    plt.show()
