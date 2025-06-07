"""
Ce script permet de faire l'intégrale d'une fontion polynomiale du troisième ordre avec la méthode de simpson
"""

from fonction import fonction_a_integrer_base
from fonction import demander_polynome

# print(f"On cherche à faire l'intégrale entre a et b d'une fonction de la forme : p1 + p2*x + p3*x**2 + p4*x**3")

# # Coefficients du polynome, demander à l'utilisateur
# coefficients = demander_polynome()

# # Bornes de l'intégrale, demander à l'utilisateur
# a = float(input('Entrez la valeur de la borne inférieure : '))
# b = float(input('Entrez la valeur de la borne supérieure : '))

# # Nombre de segments, demander à l'utilisateur
# n = float(input('Entrez le nombre de segments que vous souhaitez : '))

# # Divisions
# base_parabole = (b-a)/n

# # on initialise la valeur de l'intégrale
# integrale = 0
# # on initialise les bornes de la première parabole
# milieu = a + 0.5*base_parabole
# depart = a
# # boucle tant qu'on a pas atteint la dernière valeur sur laquelle on veut intégrer
# while depart <= b-base_parabole :
#     # on ajoute à la valeur de l'intégrale l'aire du premier rectangle
#     integrale += (base_parabole / 6) * (fonction_a_integrer_base(depart,coefficients) + 4*fonction_a_integrer_base(milieu,coefficients) + fonction_a_integrer_base(depart+base_parabole,coefficients))
#     # on ajoute la base de la parabole pour passer à la suivante
#     depart += base_parabole
#     milieu += base_parabole

# # on affiche la valeur de l'intégrale
# print(f"L'integrale de la fonction avec la méthode de simpson est : {integrale}")

def simpson_python(a, b, p1, p2, p3, p4, n):
    """
    Intégration en utilisant la méthode de Simpson.

    Paramètres:
    a (float): premier intervalle.
    b (float): dernier intervalle.
    p1, p2, p3, p4 (float): Coefficients de la fonction f(x).
    n (int): step.

    Return:
    aire (float): Le résultat de l'intégration.
    """
    # Divisions
    base_parabole = (b - a) / n
    # on initialise la valeur de l'intégrale
    integrale = 0
    # on initialise les bornes de la première parabole
    milieu = a + 0.5 * base_parabole
    depart = a
    # boucle tant qu'on a pas atteint la dernière valeur sur laquelle on veut intégrer
    while depart <= b - base_parabole:
        # on ajoute à la valeur de l'intégrale l'aire du premier rectangle
        integrale += (base_parabole / 6) * (
            fonction_a_integrer_base(depart, [p1, p2, p3, p4]) +
            4 * fonction_a_integrer_base(milieu, [p1, p2, p3, p4]) +
            fonction_a_integrer_base(depart + base_parabole, [p1, p2, p3, p4])
        )
        # on ajoute la base de la parabole pour passer à la suivante
        depart += base_parabole
        milieu += base_parabole

    return integrale