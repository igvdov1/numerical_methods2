import numpy as np

def ez_sympson(f, x, m, low_lim, high_lim, h):
    grid = np.arange(low_lim, high_lim, h)
    answer = []
    