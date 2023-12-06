import numpy as np

# def trapeze_method(f, x, m,low_lim: float, high_lim: float, dx: float = 0.1):
#     grid = np.arange(low_lim, high_lim, dx)
#     return np.sum(f(x,m, grid[:-1]) + f(x, m, grid[1:])) * dx / 2

def trapeze_method(f, x, m, grid):

    return np.sum(f(x,m, grid[:-1]) + f(x,m,grid[1:]))* (grid[1]+grid[0])/2