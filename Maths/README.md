# Bibliothèque de Fonctions Mathématiques en Python

Cette bibliothèque contient une collection de fonctions utiles pour effectuer divers calculs mathématiques. Les fonctions couvrent un large éventail de sujets, y compris l'algèbre, la trigonométrie, les statistiques, le calcul, la géométrie, et les transformations géométriques.

## Table des Matières
1. [Installation](#installation)
2. [Utilisation](#utilisation)
3. [Liste des Fonctions](#liste-des-fonctions)
    - [Algèbre](#algèbre)
    - [Trigonométrie](#trigonométrie)
    - [Statistiques](#statistiques)
    - [Calcul](#calcul)
    - [Géométrie](#géométrie)
    - [Transformations Géométriques](#transformations-géométriques)
    - [Algorithmes Numériques](#algorithmes-numériques)
    - [Mathématiques Diverses](#mathématiques-diverses)
4. [Exemples](#exemples)

## Installation

Aucune installation spéciale n'est nécessaire. Assurez-vous simplement d'avoir `numpy` et `scipy` installés dans votre environnement Python.

```bash
pip install numpy scipy
```

## Utilisation

Vous pouvez importer ce fichier dans votre script Python et appeler les fonctions directement. Voici un exemple :

```python
from math_library import pgcd, solve_quadratic

print(pgcd(48, 18))
print(solve_quadratic(2, 4, -6))
```

## Liste des Fonctions

### Algèbre
- `decomposer_en_facteurs_premiers(n)`: Décompose un nombre en facteurs premiers.
- `pgcd(a, b)`: Calcule le plus grand commun diviseur de deux nombres.
- `ppcm(a, b)`: Calcule le plus petit commun multiple de deux nombres.
- `is_prime_number(n)`: Vérifie si un nombre est premier.
- `solve_quadratic(a, b, c)`: Résout une équation quadratique.
- `solve_linear_system(A, b)`: Résout un système linéaire Ax = b.
- `matrix_determinant(A)`: Calcule le déterminant d'une matrice.
- `matrix_inverse(A)`: Calcule l'inverse d'une matrice.

### Trigonométrie
- `degrees_to_radians(degrees)`: Convertit des degrés en radians.
- `radians_to_degrees(radians)`: Convertit des radians en degrés.
- `sine(angle_radians)`: Calcule le sinus d'un angle en radians.
- `cosine(angle_radians)`: Calcule le cosinus d'un angle en radians.
- `tangent(angle_radians)`: Calcule la tangente d'un angle en radians.
- `arc_sine(value)`: Calcule l'arc sinus d'une valeur.
- `arc_cosine(value)`: Calcule l'arc cosinus d'une valeur.
- `arc_tangent(value)`: Calcule l'arc tangente d'une valeur.

### Statistiques
- `mean(data)`: Calcule la moyenne d'un ensemble de données.
- `median(data)`: Calcule la médiane d'un ensemble de données.
- `mode(data)`: Calcule le mode d'un ensemble de données.
- `variance(data)`: Calcule la variance d'un ensemble de données.
- `standard_deviation(data)`: Calcule l'écart-type d'un ensemble de données.
- `correlation_coefficient(x, y)`: Calcule le coefficient de corrélation entre deux ensembles de données.
- `covariance(x, y)`: Calcule la covariance entre deux ensembles de données.
- `percentile(data, percentile_rank)`: Calcule le percentile d'un ensemble de données.
- `skewness(data)`: Calcule l'asymétrie d'un ensemble de données.
- `kurtosis(data)`: Calcule le kurtosis d'un ensemble de données.

### Calcul
- `derivative(f, x, h=1e-7)`: Calcule la dérivée d'une fonction en un point.
- `second_derivative(f, x, h=1e-5)`: Calcule la seconde dérivée d'une fonction en un point.
- `partial_derivative(f, var, point, h=1e-5)`: Calcule la dérivée partielle d'une fonction en un point.
- `integral(f, a, b, n=1000)`: Calcule l'intégrale définie d'une fonction sur un intervalle.

### Géométrie
- `area_of_circle(radius)`: Calcule l'aire d'un cercle.
- `circumference_of_circle(radius)`: Calcule la circonférence d'un cercle.
- `area_of_triangle(base, height)`: Calcule l'aire d'un triangle.
- `area_of_rectangle(length, width)`: Calcule l'aire d'un rectangle.
- `volume_of_cube(side)`: Calcule le volume d'un cube.
- `volume_of_sphere(radius)`: Calcule le volume d'une sphère.
- `area_of_trapezoid(a, b, h)`: Calcule l'aire d'un trapèze.
- `area_of_parallelogram(base, height)`: Calcule l'aire d'un parallélogramme.
- `volume_of_cylinder(radius, height)`: Calcule le volume d'un cylindre.
- `volume_of_cone(radius, height)`: Calcule le volume d'un cône.

### Transformations Géométriques
- `translate_point(point, translation_vector)`: Translate un point par un vecteur de translation.
- `rotate_point(point, angle_degrees, origin=(0, 0))`: Tourne un point autour d'un point d'origine.
- `scale_point(point, scale_factor, origin=(0, 0))`: Échelle un point par rapport à un point d'origine.

### Algorithmes Numériques
- `bisection_method(f, a, b, tol=1e-5)`: Trouve une racine d'une fonction en utilisant la méthode de bissection.
- `newton_raphson_method(f, df, x0, tol=1e-5, max_iter=1000)`: Trouve une racine d'une fonction en utilisant la méthode de Newton-Raphson.

### Mathématiques Diverses
- `factorial(n)`: Calcule le factoriel d'un nombre.
- `factorial_recursive(n)`: Calcule le factoriel d'un nombre de manière récursive.
- `fibonacci(n)`: Génère les n premiers nombres de la suite de Fibonacci.
- `combinations(n, k)`: Calcule le nombre de combinaisons de n éléments pris k à la fois.
- `permutations(n, k)`: Calcule le nombre de permutations de n éléments pris k à la fois.
- `gcd_multiple(numbers)`: Calcule le PGCD d'une liste de nombres.
- `lcm_multiple(numbers)`: Calcule le PPCM d'une liste de nombres.
- `harmonic_mean(data)`: Calcule la moyenne harmonique d'un ensemble de données.
- `geometric_mean(data)`: Calcule la moyenne géométrique d'un ensemble de données.
- `is_perfect_square(n)`: Vérifie si un nombre est un carré parfait.
- `is_fibonacci_number(n)`: Vérifie si un nombre appartient à la suite de Fibonacci.

## Exemples

Voici quelques exemples d'utilisation des fonctions de cette bibliothèque :

```python
# Importer les fonctions
from math_library import *

# Algèbre
print("PGCD de 48 et 18:", pgcd(48, 18))
print("Solutions de l'équation quadratique 2x² + 4x - 6 = 0:", solve_quadratic(2, 4, -6))

# Trigonométrie
print("Sine de 90 degrés:", sine(degrees_to_radians(90)))

# Statistiques
print("Moyenne de [1, 2, 3, 4, 5]:", mean([1, 2, 3, 4, 5]))

# Géométrie
print("Volume d'une sphère de rayon 3:", volume_of_sphere(3))

# Algorithmes Numériques
f = lambda x: x**3 - x - 2
df = lambda x: 3*x**2 - 1
print("Racine de l'équation x^3 - x - 2 = 0 par méthode de Newton-Raphson:", newton_raphson_method(f, df, 1))

# Mathématiques Diverses
print("Factoriel de 5:", factorial(5))
print("Fibonacci des 10 premiers nombres:", fibonacci(10))
```

