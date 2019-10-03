"""
This program displays the Mandelbrot set using the implementation from http://rosettacode.org/wiki/Mandelbrot_set#
"""
__author__ = "Varun Nair"


import matplotlib.pyplot as plt
import numpy as np


def mandlebrot(npts = 300, max_iter =100):
    """
    this function takes in number of points and max no of iterations as resolution parameters and PLOTS
    a graphical representation of the mandelbrot set
    :param npts: number of points
    :param max_iter: maximum iteration
    :return: None
    """
    X = np.linspace(-2, 2, 2 * npts)
    Y = np.linspace(-2, 2, npts)
    C = X[:, None] + 1J * Y
    Z = np.zeros_like(C)
    exit_times = max_iter * np.ones(C.shape, np.int32)
    mask = exit_times > 0

    for k in range(max_iter):
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mask, old_mask = abs(Z) < 2, mask
        exit_times[mask ^ old_mask] = k

    plt.imshow(exit_times.T,
           cmap=plt.cm.prism,
           extent=(X.min(), X.max(), Y.min(), Y.max()))
    plt.show()


mandlebrot(300, 120)