import numpy as np
from fonction import fonction_a_integrer_numpy
from fonction import demander_polynome
def integrale_python(f,a,b,n) :

    longueur = (b-a)/n
    coef = demander_polynome()
    surface = 0
    indice = a + longueur/2
    while indice < b :
        surface += f(indice, coef)*longueur
        indice += longueur
    return surface

print(integrale_python(fonction_a_integrer_numpy,1, 20, 10 ))





