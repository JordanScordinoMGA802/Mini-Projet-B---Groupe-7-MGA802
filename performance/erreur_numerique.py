"""
Script permettant de calculer l'erreur numérique entre l'intégrale numérique et l'intégrale réelle/
"""
import numpy as np

from integration_numerique.numpy.Rectangle_numpy import integrale_numpy_perf
from fonction import integrer_polynome_reel
from fonction_perf import polynome_aleatoire_perf


# Initialization: on recupère une fonction f(x) à intégrer
a = -10
b = 10
function_a_tester = polynome_aleatoire_perf()
print(f"Voici le polynôme que l'on va intégrer pour le test de performance: {function_a_tester}")

# Liste vide qui va contenir la valeur de l'erreur pour un indice n
erreur_rectangle_numpy = []

# Pour n allant de 1 à 1000, on calcule l'erreur entre l'intégrale réelle et l'intégrale numérique, et on stock ce resultat dans la liste associée
for i in range(1,1000):
    erreur_rectangle_numpy.append(np.abs(integrer_polynome_reel(a,b,function_a_tester.coef) - integrale_numpy_perf(function_a_tester, a, b, i)))
