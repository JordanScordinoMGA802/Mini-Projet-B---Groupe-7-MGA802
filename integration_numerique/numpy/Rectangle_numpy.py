import numpy as np
from numpy.ma.core import cumsum

def integrale_numpy_rect(f,a,b,n) :

    longueur = (b-a)/n

    x = np.linspace(a, b, n+1)

    # On prend x0, x1, .., xn-1 et on leur soustrait x1, x2, ..., xn puis on divise par 2. Donc c'est le point entre
    #xi et xi+1
    x = (x[:-1] + x[1:]) / 2
    polynome = f(x)
    aire = longueur * polynome
    return np.sum(aire)
