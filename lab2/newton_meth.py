import numpy as np

def newton_method(x0, f,derivative, eps=1e-8):
    x2 = x0 + 1
    count = 0


    while (abs(x0 - x2) > eps):

        x1 = x0 - f(x0) / derivative(x0)
        x2 = x0
        x0 = x1
        count += 1
        


    return np.round(x2, 6), count