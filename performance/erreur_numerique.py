"""
Script permettant de calculer l'erreur numérique entre l'intégrale numérique et l'intégrale réelle/
"""
import numpy as np
import matplotlib.pyplot as plt
from fonction_perf import polynome_aleatoire_perf

# Initialization: on recupère une fonction f(x) à intégrer
function_a_tester = polynome_aleatoire_perf()
print(f"Voici le polynôme que l'on va intégrer pour le test de performance: {function_a_tester}")

