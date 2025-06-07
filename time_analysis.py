import matplotlib.pyplot as plt

from integration_numerique.numpy.Rectangle_numpy import integrale_python_perf
from integration_numerique.python.rectangle_python import rectangle_python
from integration_numerique.python.trapeze_python import trapeze_python
from trapeze_numpy import integ_trapeze_numpy
from trapeze_numpy import integ_trapeze_numpy_auto
from integration_numerique.python.simpson_python import simpson_python
from simpson_numpy import integral_simpson_numpy
from numpy import mean
from time import perf_counter 

polynome_de_test = [1, 2, 3, 4]  # Coefficients du polynôme de test
# Bornes de l'intégrale de test
a = 0
b = 10
n=1000
# Initialisation des listes pour stocker les temps d'exécution
tab_rect_times = []
tab_trap_times = []
tab_simp_times = []
tab_numpy_rect_times = []
tab_numpy_trap_times = []
tab_numpy_simp_times = []
tab_numpy_trap_times_auto = []



for i in range(100):
        # Mesure du temps pour la méthode des rectangles
        start_time = perf_counter()
        rectangle_result = rectangle_python(a, b, *polynome_de_test, n)
        rectangle_time = perf_counter() - start_time
        tab_rect_times.append(rectangle_time)

        # Mesure du temps pour la méthode des trapèzes
        start_time = perf_counter()
        trapeze_result = trapeze_python(a, b, *polynome_de_test, n)
        trapeze_time = perf_counter() - start_time
        tab_trap_times.append(trapeze_time)

        # Mesure du temps pour la méthode de Simpson
        start_time = perf_counter()
        simpson_result = simpson_python(a, b, *polynome_de_test, n)
        simpson_time = perf_counter() - start_time
        tab_simp_times.append(simpson_time)
    
            # Mesure du temps pour la méthode NumPy des rectangles
        start_time = perf_counter()
        numpy_rectangle_result = integrale_python_perf(lambda x: sum(c * x**i for i, c in enumerate(polynome_de_test)), a, b, n)
        numpy_rectangle_time = perf_counter() - start_time
        tab_numpy_rect_times.append(numpy_rectangle_time)

        # Mesure du temps pour la méthode NumPy des trapèzes
        start_time = perf_counter()
        numpy_trapeze_result_auto = integ_trapeze_numpy_auto(a, b, *polynome_de_test, n)
        numpy_trapeze_time_auto = perf_counter() - start_time
        tab_numpy_trap_times_auto.append(numpy_trapeze_time_auto)

        # Mesure du temps pour la méthode NumPy des trapèzes
        start_time = perf_counter()
        numpy_trapeze_result = integ_trapeze_numpy(a, b, *polynome_de_test, n)
        numpy_trapeze_time = perf_counter() - start_time
        tab_numpy_trap_times.append(numpy_trapeze_time)

        # Mesure du temps pour la méthode NumPy de Simpson
        start_time = perf_counter()
        numpy_simpson_result = integral_simpson_numpy(a, b, *polynome_de_test, n)
        numpy_simpson_time = perf_counter() - start_time
        tab_numpy_simp_times.append(numpy_simpson_time)


print(f"n={n}:")
print(f"  Rectangle: {rectangle_result} in {rectangle_time:.6f} seconds")
print(f"  Trapèze: {trapeze_result} in {trapeze_time:.6f} seconds")
print(f"  Simpson: {simpson_result} in {simpson_time:.6f} seconds")
print(f"  NumPy Rectangle: {numpy_rectangle_result} in {numpy_rectangle_time:.6f} seconds")
print(f"  NumPy Trapèze: {numpy_trapeze_result} in {numpy_trapeze_time:.6f} seconds")
print(f"  NumPy Simpson: {numpy_simpson_result} in {numpy_simpson_time:.6f} seconds")

print(f"  Moyenne NumPy Trapèze Auto: {mean(tab_numpy_trap_times_auto)} seconds")
print(f"  Moyenne Rectangle: {mean(tab_rect_times)} seconds")
print(f"  Moyenne Trapèze: {mean(tab_trap_times)} seconds")
print(f"  Moyenne Simpson: {mean(tab_simp_times)} seconds")
print(f"  Moyenne NumPy Rectangle: {mean(tab_numpy_rect_times)} seconds")
print(f"  Moyenne NumPy Trapèze: {mean(tab_numpy_trap_times)} seconds")
print(f"  Moyenne NumPy Simpson: {mean(tab_numpy_simp_times)} seconds")


labels = [
    "Rectangle",
    "Trapèze",
    "Simpson",
    "NumPy Rectangle",
    "NumPy Trapèze",
    "NumPy Simpson",
    "NumPy Trapèze Auto"
]
moyennes = [
    mean(tab_rect_times),
    mean(tab_trap_times),
    mean(tab_simp_times),
    mean(tab_numpy_rect_times),
    mean(tab_numpy_trap_times),
    mean(tab_numpy_simp_times),
    mean(tab_numpy_trap_times_auto)
]

plt.figure(figsize=(10, 6))
plt.bar(labels, moyennes)
plt.ylabel("Temps moyen (secondes)")
plt.title("Comparaison des temps d'exécution moyens par méthode")
plt.xticks(rotation=30)
plt.tight_layout()
print("labels:", labels)
print("moyennes:", moyennes)
plt.show(block=True)


n_values = [2,10, 100, 1000,5000, 10000,100000,1000000]  # Valeurs de n pour l'analyse de performance
rect_means = []
trap_means = []
simp_means = []
numpy_rect_means = []
numpy_trap_means = []
numpy_simp_means = []
numpy_trap_auto_means = []

for n in n_values:
    tab_rect_times = []
    tab_trap_times = []
    tab_simp_times = []
    tab_numpy_rect_times = []
    tab_numpy_trap_times = []
    tab_numpy_simp_times = []
    tab_numpy_trap_times_auto = []

    for _ in range(20):  # 20 répétitions pour la moyenne
        start_time = perf_counter()
        rectangle_python(a, b, *polynome_de_test, n)
        tab_rect_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        trapeze_python(a, b, *polynome_de_test, n)
        tab_trap_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        simpson_python(a, b, *polynome_de_test, n)
        tab_simp_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        integrale_python_perf(lambda x: sum(c * x**i for i, c in enumerate(polynome_de_test)), a, b, n)
        tab_numpy_rect_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        integ_trapeze_numpy(a, b, *polynome_de_test, n)
        tab_numpy_trap_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        integral_simpson_numpy(a, b, *polynome_de_test, n)
        tab_numpy_simp_times.append(perf_counter() - start_time)

        start_time = perf_counter()
        integ_trapeze_numpy_auto(a, b, *polynome_de_test, n)
        tab_numpy_trap_times_auto.append(perf_counter() - start_time)

    rect_means.append(mean(tab_rect_times))
    trap_means.append(mean(tab_trap_times))
    simp_means.append(mean(tab_simp_times))
    numpy_rect_means.append(mean(tab_numpy_rect_times))
    numpy_trap_means.append(mean(tab_numpy_trap_times))
    numpy_simp_means.append(mean(tab_numpy_simp_times))
    numpy_trap_auto_means.append(mean(tab_numpy_trap_times_auto))

plt.figure(figsize=(10, 6))
plt.plot(n_values, rect_means, marker='o', label="Rectangle")
plt.plot(n_values, trap_means, marker='o', label="Trapèze")
plt.plot(n_values, simp_means, marker='o', label="Simpson")
plt.plot(n_values, numpy_rect_means, marker='o', label="NumPy Rectangle")
plt.plot(n_values, numpy_trap_means, marker='o', label="NumPy Trapèze")
plt.plot(n_values, numpy_simp_means, marker='o', label="NumPy Simpson")
plt.plot(n_values, numpy_trap_auto_means, marker='o', label="NumPy Trapèze Auto")
plt.xlabel("n (nombre de subdivisions)")
plt.ylabel("Temps moyen (secondes)")
plt.title("Temps d'exécution en fonction de n")
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.tight_layout()
plt.show(block=True)