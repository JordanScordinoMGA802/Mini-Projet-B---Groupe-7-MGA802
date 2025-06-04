########## Methode Integration Trapz Numpy ##########
import numpy as np
from numpy.polynomial import Polynomial

from fonction import fonction_a_integrer_numpy

def integ_trapeze_numpy(a,b,fonction,n):
    """
    Intégration en utilisant la méthode des trapèzes avec numpy en vectorisé.

    Paramètres:
    a (float): premier intervalle.
    b (float): dernier intervalle.
    p1, p2, p3, p4 (float): Coefficients de la fonction f(x).
    n (int): step.

    Return:
    aire (float): Le résultat de l'intégration.
    """
    # Vecteur avec toutes les valeurs de x entre a et b
    x = np.linspace(a, b, n)
    # Polynome de la fonction pour tout les x
    poly = fonction(x)
    #poly=p1 + p2*x + p3*x**2 + p4*x**3
    # On calcule l'aire en utilisant la fonction des trapèzes
    # On utilise [1:] et [:-1] pour éviter de faire un for et de ne pas sélectionner la première et la dernière valeur
    aires = (poly[1:] + poly[:-1]) / 2 * (x[1:] - x[:-1])
    # On fait la somme de tous les trapèzes
    aire= aires.cumsum()[-1]
    
    return aire

def integ_trapeze_numpy_auto(a,b,fonction,n):
    """
    Intégration en utilisant la méthode de numpy.

    Paramètres:
    a (float): premier intervalle.
    b (float): dernier intervalle.
    p1, p2, p3, p4 (float): Coefficients de la fonction f(x).
    n (int): step.

    Return:
    aire (float): Le résultat de l'intégration.
    """
    # Vecteur avec toutes les valeurs de x entre a et b
    x= np.linspace(a, b, n)
    # Polynome de la fonction pour tout les x
    poly= fonction(x)
    # Utilisation de la fonction trapezoid fournie par numpy
    aire=np.trapezoid(poly, x)
    
    return aire