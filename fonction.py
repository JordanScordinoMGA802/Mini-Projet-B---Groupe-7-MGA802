from numpy.polynomial import Polynomial

def demander_coeff(coeff):
    while True:
        val_coeff = input(f"Entrez le coefficient {coeff}:")
        try:
            val_coeff = float(val_coeff)

        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue
        else:
            return val_coeff


def demander_polynome():
    coefficients = []
    print("Soit un polynome f(x) = p1 + p2.x + p3.x² = p4.x³.")
    coefficients.append(demander_coeff("p1"))
    coefficients.append(demander_coeff("p2"))
    coefficients.append(demander_coeff("p3"))
    coefficients.append(demander_coeff("p4"))

    return coefficients

def fonction_a_integrer_base(x):
    coefficients = demander_polynome()
    return coefficients[0] + coefficients[1]*x + coefficients[2]*(x**2) + coefficients[3]*(x**3)

def fonction_a_integrer_numpy(x):
    coefficients = demander_polynome()
    return Polynomial(coefficients)(x)
