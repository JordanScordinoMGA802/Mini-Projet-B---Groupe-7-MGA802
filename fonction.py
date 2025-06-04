"""
:file: fonction.py
:brief: Ensemble de fonction permettant de demander les coefficients d'un polynome du 3ème ordre.
"""
import numpy as np
from numpy.polynomial import Polynomial

def demander_coeff(coeff):
    """
    Demande à l'utilisateur de rentrer un coefficient, un float, et retourne ce float.
    :param coeff: Le nom du coefficient à demander.
    :return: Le coefficient.
    """
    while True:
        val_coeff = input(f"Entrez le coefficient {coeff}:")

        # On essaie de convertir le coefficient en float
        try:
            val_coeff = float(val_coeff)

        # Si la conversion n'est pas possible, on va redemander le coefficient
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # Le coefficient est valide, on le retourne
        else:
            return val_coeff


def demander_polynome():
    """
    Demande de rentrer les 4 coefficients d'un polynome et les retourne dans une liste.
    :return: Une liste de coefficients.
    """
    coefficients = []
    print("Soit un polynome f(x) = p4.x³ + p3.x² + p2.x = p1.x.")
    coefficients.append(demander_coeff("p1"))
    coefficients.append(demander_coeff("p2"))
    coefficients.append(demander_coeff("p3"))
    coefficients.append(demander_coeff("p4"))

    return coefficients

def fonction_a_integrer_base(x, coefficients):
    """
    Calcul la valeur en x d'un polynôme d'ordre 3
    :param x:
    :param coefficients: Les coefficients du polynome.
    :return: La valeur du polynome en x.
    """
    return coefficients[0]*(x**3) + coefficients[1]*(x**2) + coefficients[2]*x+ coefficients[3]

def fonction_a_integrer_numpy(x, coefficients):
    """
    Calcul la valeur en x d'un polynôme à l'aide de numpy
    :param x:
    :param coefficients: Les coefficients du polynome.
    :return: La valeur du polynome en x.
    """
    return Polynomial(coefficients)(x)

def integrer_polynome_reel(a,b,coefficients):
    """
    Retourne l'intégrale entre a et b d'un polynôme d'ordre 3.
    :param a: la borne inferieure de l'intégrale
    :param b: la borne superieur de l'integrale
    :param coefficients: Les coefficients du polynome.
    :return: La valeur de l'intégrale, un float
    """

    # Si a > b, on lève une exception
    if a > b:
        raise ValueError

    # Peut lever une exception si le cast en float est impossible!
    a = float(a)
    b = float(b)

    if a == b:
        return 0.0

    polynome_integre = np.polyint(np.poly1d(coefficients))
    return polynome_integre(b)-polynome_integre(a)
