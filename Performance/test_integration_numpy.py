from Rectangle_numpy import integrale_python_perf

from fonction_perf import fonction_a_integrer_numpy_perf

a = input('Quel est la valeur de a :')
b = input('Quel est la valeur de b :')
f = fonction_a_integrer_numpy_perf()
print(integrale_python_perf(f))
