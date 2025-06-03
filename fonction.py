from numpy.polynomial import Polynomial

def fonction_a_integrer_base(x):
    coefficients = (1, 2, 5, 4)
    return coefficients[0] + coefficients[1]*x + coefficients[2]*(x**2) + coefficients[3]*(x**3)

def fonction_a_integrer_numpy(x):
    coefficients = (1, 2, 5, 4)
    return Polynomial(coefficients)(x)
