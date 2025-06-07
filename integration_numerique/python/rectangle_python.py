"""
Ce script permet de faire l'intégrale d'une fontion polynomiale du troisième ordre avec la méthode des rectangles
"""

from fonction import fonction_a_integrer_base
from fonction import demander_polynome
def rectangle_python(a,b,p1,p2,p3,p4,n):
    """
    Intégration en utilisant la méthode des rectangles.

    Paramètres:
    a (float): premier intervalle.
    b (float): dernier intervalle.
    p1, p2, p3, p4 (float): Coefficients de la fonction f(x).
    n (int): step.

    Return:
    aire (float): Le résultat de l'intégration.
    """
    # Divisions
    base_rectangle = (b-a)/n
    coefficients = [p1, p2, p3, p4]
    # on initialise la valeur de l'intégrale
    integrale = 0
    # on démarre au milieu de la base du premier rectangle à partir de la borne inférieure
    depart = a + 0.5*base_rectangle
    # boucle tant qu'on a pas atteint la dernière valeur sur laquelle on veut intégrer
    while depart <= b-base_rectangle :
        # on ajoute à la valeur de l'intégrale l'aire du premier rectangle
        integrale += fonction_a_integrer_base(depart,coefficients)* base_rectangle
        depart += base_rectangle

    # on affiche la valeur de l'intégrale
    print(f"L'integrale de la fonction avec la méthode des retangles est : {integrale}")

    return integrale


# print(f"On cherche à faire l'intégrale entre a et b d'une fonction de la forme : p1 + p2*x + p3*x**2 + p4*x**3")

# # Coefficients du polynome
# coefficients = demander_polynome()

# # Bornes de l'intégrales
# a = float(input('Entrez la valeur de la borne inférieure : '))
# b = float(input('Entrez la valeur de la borne supérieure : '))

# # Nombre de segments
# n = float(input('Entrez le nombre de segments que vous souhaitez : '))

# # Divisions
# base_rectangle = (b-a)/n

# # on initialise la valeur de l'intégrale
# integrale = 0
# # on démarre au milieu de la base du premier rectangle à partir de la borne inférieure
# depart = a + 0.5*base_rectangle
# # boucle tant qu'on a pas atteint la dernière valeur sur laquelle on veut intégrer
# while depart <= b-base_rectangle :
#     # on ajoute à la valeur de l'intégrale l'aire du premier rectangle
#     integrale += fonction_a_integrer_base(depart,coefficients)* base_rectangle
#     depart += base_rectangle

# # on affiche la valeur de l'intégrale
# print(f"L'integrale de la fonction avec la méthode des retangles est : {integrale}")

