import numpy as np
from fonction.py import fonction_a_intergrer_numpy
def integrale_python(f,a,b,n) :

    longueur = (b-a)/n
    surface = 0
    for i in range(b-a):
       surface += f(2)*longueur

       return surface

integrale_python(fonction_a_intergrer_numpy,1, 20, 10 )




