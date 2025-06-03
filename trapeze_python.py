"""
Ce script permet de faire l'intégrale d'une fontion polynomiale du troisième ordre avec la méthode des trapèze
"""

from fonction import fonction_a_integrer_base
from fonction import demander_polynome

print(f"On cherche à faire l'intégrale entre a et b d'une fonction de la forme : p1 + p2*x + p3*x**2 + p4*x**3")

# Coefficient du polynome
coefficient = demander_polynome()

# Bornes de l'intégrales
a = float(input('Entrez la valeur de la borne inférieure : '))
b = float(input('Entrez la valeur de la borne supérieure : '))

# Nombre de segments
n = float(input('Entrez le nombre de segments que vous souhaitez : '))

# Divisions
base_trapeze = (b-a)/n

# on initialise la valeur de l'intégrale
integrale = 0
# on démarre à la borne inférieure
depart = a
# boucle tant qu'on a pas atteint la dernière valeur sur laquelle on veut intégrer
while depart <= b-base_trapeze :
    # on ajoute à la valeur de l'intégrale l'aire du premier rectangle
    integrale += base_trapeze * (fonction_a_integrer_base(depart,coefficient) + fonction_a_integrer_base(depart+base_trapeze,coefficient)) / 2
    depart += base_trapeze

# on affiche la valeur de l'intégrale
print(f"L'integrale de la fonction avec la méthode des trapèzes est : {integrale}")