"""
Script permettant de calculer l'erreur numérique entre l'intégrale numérique et l'intégrale réelle/
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
coefficients = np.random.uniform(-1, 1, size=(4,))*10
# importe les fonctions personelles
from integration_numerique.numpy.Rectangle_numpy import integrale_numpy_rect
from integration_numerique.numpy.trapeze_numpy import integ_trapeze_numpy
from integration_numerique.numpy.simpson_numpy import integral_simpson_numpy
from integration_numerique.python.rectangle_python import rectangle_python
from integration_numerique.python.trapeze_python import trapeze_python
from integration_numerique.python.simpson_python import simpson_python

from fonctions.fonction import integrer_polynome_reel
from fonctions.fonction_perf import polynome_aleatoire_perf


# Initialization: on recupère une fonction f(x) à intégrer
a = -10
b = 10
function_a_tester = polynome_aleatoire_perf()
print(f"Voici le polynôme que l'on va intégrer pour le test de performance: {function_a_tester}")

# Liste vide qui va contenir la valeur de l'erreur pour un indice n
erreur_rectangle_numpy = []
erreur_trapeze_numpy = []
erreur_simpson_numpy = []
erreur_rectangle_python = []
erreur_trapeze_python = []
erreur_simpson_python = []

# Pour n allant de 1 à 1000, on calcule l'erreur entre l'intégrale réelle et l'intégrale numérique, et on stock ce resultat dans la liste associée
for i in range(1,200):
    integrale_reelle = integrer_polynome_reel(a,b,function_a_tester.coef)
    erreur_rectangle_numpy.append(np.abs(integrale_reelle - integrale_numpy_rect(function_a_tester, a, b, i)))
    erreur_trapeze_numpy.append(np.abs(integrale_reelle - integ_trapeze_numpy(a, b, function_a_tester, i)))
    erreur_simpson_numpy.append(np.abs(integrale_reelle - integral_simpson_numpy(a,b,function_a_tester,i)))
    erreur_rectangle_python.append(abs(integrale_reelle - rectangle_python(a,b,coefficients[0],coefficients[1],coefficients[2],coefficients[3],i)))
    erreur_trapeze_python.append(abs(integrale_reelle - trapeze_python(a, b, coefficients[0],coefficients[1],coefficients[2],coefficients[3],i)))
    erreur_simpson_python.append(abs(integrale_reelle - simpson_python(a, b, coefficients[0],coefficients[1],coefficients[2],coefficients[3],i)))

# Plotting

plt.rcParams['font.size'] = 12
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

# plt.figure(figsize=(8,5))
# #plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
# plt.plot(erreur_rectangle_numpy,label='Intégrale rectangulaire Numpy',color='red',linewidth=3.0)
# plt.plot(erreur_trapeze_numpy,label='Intégrale trapezoïdale Numpy',color='blue',linewidth=3.0)
# plt.plot(erreur_simpson_numpy,label='Intégrale Simpson Numpy',color='green',linewidth=3.0)
# plt.plot(erreur_rectangle_python,label='Intégrale Rectangle Python',color='yellow',linewidth=3.0)
# plt.plot(erreur_trapeze_python,label='Intégrale Trapeze Python',color='pink',linewidth=3.0)
# plt.plot(erreur_simpson_python,label='Intégrale Simpson Python',color='black',linewidth=3.0)
#
# plt.title("Erreur de l'intégrale numérique")
# plt.xlim(0,len(erreur_rectangle_numpy))
# plt.xlabel("Nombre d'incréments")
# plt.ylabel("Erreur")
# plt.grid()
# plt.legend()
# plt.savefig('../../ressources/erreur_integral_numpy.pdf')
# plt.show()

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(erreur_trapeze_numpy,label='Intégrale trapezoïdale Numpy',color='blue',linewidth=3.0)
plt.plot(erreur_trapeze_python,label='Intégrale Trapeze Python',color='pink',linewidth=3.0)

plt.title("Erreur de l'intégrale numérique")
plt.xlim(0,len(erreur_rectangle_numpy))
plt.xlabel("Nombre d'incréments")
plt.ylabel("Erreur")
plt.grid()
plt.legend()
plt.savefig('../../ressources/erreur_integral_trapezoidale.png')
plt.show()

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(erreur_rectangle_numpy,label='Intégrale rectangulaire Numpy',color='red',linewidth=3.0)
plt.plot(erreur_rectangle_python,label='Intégrale Rectangle Python',color='yellow',linewidth=3.0)

plt.title("Erreur de l'intégrale rectangulaire numérique")
plt.xlim(0,len(erreur_rectangle_numpy))
plt.xlabel("Nombre d'incréments")
plt.ylabel("Erreur")
plt.grid()
plt.legend()
plt.savefig('../../ressources/erreur_integral_rectangulaire.png')
plt.show()


plt.plot(erreur_simpson_numpy,label='Intégrale Simpson Numpy',color='green',linewidth=3.0)
plt.plot(erreur_simpson_python,label='Intégrale Simpson Python',color='black',linewidth=3.0)

plt.title("Erreur de l'intégrale numérique")
plt.xlim(0,len(erreur_rectangle_numpy))
plt.xlabel("Nombre d'incréments")
plt.ylabel("Erreur")
plt.grid()
plt.legend()
plt.savefig('../../ressources/erreur_integral_simpson.png')
plt.show()

plt.figure(figsize=(8,5))
#plt.fill_between(data.index,data['min_temp'],data['max_temp'],alpha=0.5,color='gray')
plt.plot(erreur_trapeze_numpy,label='Intégrale trapezoïdale Numpy',color='blue',linewidth=3.0)
plt.plot(erreur_trapeze_python,label='Intégrale Trapeze Python',color='pink',linewidth=3.0)