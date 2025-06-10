"""
Ce programme permettra de tracer la convergence de toutes les fonctions
"""

from matplotlib import pyplot as plt

# On importe les fonctions créées
# Numpy
from integration_numerique.numpy.Rectangle_numpy import integrale_numpy_rect
from integration_numerique.numpy.simpson_numpy import *
from integration_numerique.numpy.trapeze_numpy import *

# Python de base
from integration_numerique.python.simpson_python import simpson_python
from integration_numerique.python.trapeze_python import trapeze_python
from integration_numerique.python.rectangle_python import rectangle_python

from fonctions.fonction_perf import polynome_aleatoire_perf

import numpy as np
from scipy.integrate import simpson

# Initialization: on recupère une fonction f(x) à intégrer
a = -10
b = 10
function_a_tester = polynome_aleatoire_perf()
print(f"Voici le polynôme que l'on va intégrer pour le test de performance: {function_a_tester}")
coefficients = function_a_tester.coef
p1 = coefficients[0]
p2 = coefficients[1]
p3 = coefficients[2]
p4 = coefficients[3]


# on fait le choix de comparer la convergence pour les même méthodes
# rectangle
# Initialistion des données à tracer
liste_segment = []
liste_resultats_rect_numpy = []
liste_resultats_rect_python = []

for n in range(1,500):
    liste_segment.append(n)
    liste_resultats_rect_numpy.append(integrale_numpy_rect(function_a_tester,a,b,n))
    liste_resultats_rect_python.append(rectangle_python(a,b,p1,p2,p3,p4,n))

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(liste_segment,liste_resultats_rect_numpy,label='Intégrale rectangulaire Numpy',color='red',linewidth=3.0)
plt.plot(liste_segment,liste_resultats_rect_python,label='Intégrale rectangulaire python',color='blue',linewidth=3.0)
plt.title("Convergence de la méthode des rectangles")
plt.xlim(0,len(liste_segment))
plt.xlabel("Nombre de segment")
plt.ylabel("Résultat intégrale")
plt.grid()
plt.legend()
#plt.savefig('../../ressources/convergence.pdf')
plt.show()


# trapèze
# Initialistion des données à tracer
liste_segment_trap = []
liste_resultats_trap_numpy = []
liste_resultats_trap_python = []
liste_resultats_trap_pp = []

for n in range(1,500):
    liste_segment_trap.append(n)
    liste_resultats_trap_numpy.append(integ_trapeze_numpy(a,b,function_a_tester,n))
    liste_resultats_trap_python.append(trapeze_python(a,b,p1,p2,p3,p4,n))
    liste_resultats_trap_pp.append(integ_trapeze_numpy_auto(a, b, function_a_tester, n))

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(liste_segment_trap,liste_resultats_trap_numpy,label='Intégrale trapèze Numpy',color='red',linewidth=3.0)
plt.plot(liste_segment_trap,liste_resultats_trap_python,label='Intégrale trapèze Python',color='blue',linewidth=3.0)
plt.plot(liste_segment_trap,liste_resultats_trap_pp,label='Intégrale trapèze pré-programmée',color='green',linewidth=2.0)
plt.title("Convergence de la méthode des trapèzes")
plt.xlim(0,len(liste_segment_trap))
plt.xlabel("Nombre de segment")
plt.ylabel("Résultat intégrale")
plt.grid()
plt.legend()
#plt.savefig('../../ressources/convergence.pdf')
plt.show()


# simpson
# Initialistion des données à tracer
liste_segment_simp = []
liste_resultats_simp_numpy = []
liste_resultats_simp_python = []
liste_resultats_simp_pp = []

for n in range(1,500):
    liste_segment_simp.append(n)
    liste_resultats_simp_numpy.append(integral_simpson_numpy(a,b,function_a_tester,n))
    liste_resultats_simp_python.append(simpson_python(a,b,p1, p2, p3, p4, n))
    liste_resultats_simp_pp.append(simpson_pp(a,b,p1,p2,p3,p4,n))


plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
#plt.plot(liste_segment_simp,liste_resultats_simp_numpy,label='Intégrale simpson Numpy',color='red',linewidth=3.0)
plt.plot(liste_segment_simp,liste_resultats_simp_python,label='Intégrale simpson Python',color='blue',linewidth=3.0)
plt.plot(liste_segment_simp,liste_resultats_simp_pp,label='Intégrale simpson pré-programmé',color='green',linewidth=3.0)
plt.title("Convergence de la méthode simpson")
plt.xlim(0,len(liste_segment_simp))
plt.xlabel("Nombre de segment")
plt.ylabel("Résultat intégrale")
plt.grid()
plt.legend()
#plt.savefig('../../ressources/convergence.pdf')
plt.show()