import numpy as np
from numpy.polynomial import Polynomial

def fonction_a_integrer_base_perf(x):
    coefficients = np.random.uniform(-1, 1, size=(4,))*10

    return coefficients[0] + coefficients[1]*x + coefficients[2]*(x**2) + coefficients[3]*(x**3)

def fonction_a_integrer_numpy_perf(x):
    coefficients = np.random.uniform(-1, 1, size=(4,))*10
    return Polynomial(coefficients)(x)
