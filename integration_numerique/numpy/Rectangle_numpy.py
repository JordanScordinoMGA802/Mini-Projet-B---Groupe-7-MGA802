import numpy as np
from fonctions.fonction import fonction_a_integrer_numpy
from fonctions.fonction import demander_polynome
from time import perf_counter
def integrale_numpy_perf(f,a,b,n) :

    longueur = (b-a)/n
    surface = 0
    indice = a + longueur/2
    while indice < b :
        surface += f(indice)*longueur
        indice += longueur
    return surface





