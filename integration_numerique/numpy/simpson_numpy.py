################################ Integral de simpson avec numpy ################################

import numpy as np

def integral_simpson_numpy(a,b,function,n):
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
    x = np.linspace(a, b, n+1)
    x_ab = (x[1:] + x[:-1]) / 2
    poly=function(x)
    # Polynome de la fonction pour tout les x
    poly_ab=function(x_ab)
    # On calcule l'aire en utilisant la fonction des trapèzes
    # On utilise [1:] et [:-1] pour éviter de faire un for et de ne pas sélectionner la première et la dernière valeur
    aires = ((x[1:] - x[:-1])/6)*((poly[1:] + poly[:-1]) +4*poly_ab) 
    # On fait la somme de tous les trapèzes
    aire= aires.cumsum()[-1]
    
    return aire