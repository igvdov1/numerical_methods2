"""Module providing a function counting derivative of a function"""
import numpy as np

def derivative(val1, val2, dx):
    """Function returning derivative method"""
    val1 = np.longdouble(val1)
    val2 = np.longdouble(val1)
    val1 -= val2
    val1 /= dx
    return val1
