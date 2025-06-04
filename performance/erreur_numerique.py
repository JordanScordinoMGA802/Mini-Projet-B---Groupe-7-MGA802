"""
Script permettant de calculer l'erreur numérique entre l'intégrale numérique et l'intégrale réelle/
"""
import numpy as np
import matplotlib.pyplot as plt

# importe les fonctions personelles
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
for i in range(1,10):
    erreur_rectangle_numpy.append(np.abs(integrer_polynome_reel(a,b,function_a_tester.coef) - integrale_numpy_perf(function_a_tester, a, b, i)))

# Plotting

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(erreur_rectangle_numpy,label='Intégrale rectangulaire Numpy',color='red',linewidth=3.0)
plt.title("Erreur de l'intégrale numérique")
plt.xlim(0,len(erreur_rectangle_numpy))
plt.xlabel("Nombre d'incréments")
plt.ylabel("Erreur")
plt.grid()
plt.legend()
plt.savefig('../images/erreur_int_rect_numpy.pdf')
plt.show()