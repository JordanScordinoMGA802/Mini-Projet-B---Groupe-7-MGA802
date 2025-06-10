"""
:brief: Programme principal permettant de calculer l'intégrale d'un polynome selon la méthode d'intégration numérique
de notre choix.
"""
import unicodedata

from numpy.polynomial import Polynomial

from fonctions.fonction import demander_polynome
from integration_numerique.numpy.Rectangle_numpy import integrale_numpy_rect
from integration_numerique.numpy.simpson_numpy import integral_simpson_numpy
from integration_numerique.numpy.trapeze_numpy import integ_trapeze_numpy
7
# Provient de notre projet précédent, code César
def retirer_accents(input_str):
    """
    Supprime les accents d'une chaîne de character.
    :param input_str: Chaîne de caractère dont on veut retirer les accents.
    :return: La chaîne de character sans accents.
    """

    # Replace all special character by their compatible equivalent
    nfkd_form = unicodedata.normalize('NFKD', input_str)

    # Create a new str '' and append each character from the normalized form
    res = ''.join([c for c in nfkd_form if not unicodedata.combining(c)])
    return res

def demander_methode_integration():
    """
    Demande à l'utilisateur quelle méthode d'intégration souhaite-t-il utiliser.
    :return: la méthode à utiliser, sans accents.
    """
    while True:
        methode = retirer_accents(input(f"Sélectionnez une méthode d'intégration (rectangle/trapeze/simpson):").lower())

        # On vérifie que la réponse soit valide
        if methode not in ['rectangle', 'trapeze', 'simpson']:
            print("Veuillez entrer une réponse valide. (rectangle/trapeze/simpson)")
            continue

        else:
            return methode

def demander_parametres(coeff):
    """
    Demande à l'utilisateur de rentrer un coefficient, un float, et retourne ce float.
    :param coeff: Le nom du coefficient à demander.
    :return: Le coefficient.
    """
    while True:
        val_coeff = input(f"Entrez le paramètre {coeff}. Ce doit être un entier.")

        # On essaie de convertir le coefficient en float
        try:
            val_coeff = int(val_coeff)

        # Si la conversion n'est pas possible, on va redemander le coefficient
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # Le coefficient est valide, on le retourne
        else:
            return val_coeff

def demander_n():
    """
    Demande à l'utilisateur d'entrer l'entier n ert s'assure que n soit un entier positif.
    """
    while True:
        n = input(f"Entrez le paramètre n. Ce doit être un entier positif.")

        # On essaie de convertir le coefficient en float
        try:
            n = int(n)

        # Si la conversion n'est pas possible, on va redemander le coefficient
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # Le coefficient est valide, on le retourne
        else:
            if n <= 0:
                print("Veuillez entrer un nombre positif.")
                continue

            else:
                return n

def main():
    """
    Programme principal
    :return:
    """

    coefficients = demander_polynome()
    polynome = Polynomial(coefficients)
    methode = demander_methode_integration()

    a = demander_parametres('a')
    b = demander_parametres('b')
    n = demander_n()

    # L'intégrale est négative si a est plus grand que b.
    if a > b:
        tmp = a
        a = b
        b = tmp
        result = -1

    else:
        result = 1

    if methode == 'rectangle':
        result *=  integrale_numpy_rect(polynome, a, b, n)
    elif methode == 'trapeze':
        result *=  integ_trapeze_numpy(a, b, polynome, n)
    else:
        result *=  integral_simpson_numpy(a, b, polynome, n)

    print(f"Le résultat de l'intégrale avec la méthode f{methode} est: {result:.3f}")

if __name__ == "__main__":
    main()
