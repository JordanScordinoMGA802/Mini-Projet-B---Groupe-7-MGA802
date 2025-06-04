from Rectangle_numpy import integrale_python_perf

from fonction_perf import fonction_a_integrer_numpy_perf

a = input('Quel est la valeur de a :')
b = input('Quel est la valeur de b :')
n = input('Quel est la valeur de n :')
f = fonction_a_integrer_numpy_perf
print(integrale_python_perf(fonction_a_integrer_numpy_perf,'a','b','n'))
nb_repetition= 100
from timeit import timeit
total_time = timeit(f'fonction performance({f} , {a} , {b} , {n})',
    globals=globals())  # cet argument permet de transférer les variables connues dans le script
    #number=nb_repetition
print(f"Temps d'execution moyen avec timeit: {1000.*(total_time/nb_repetition)} [ms]")
