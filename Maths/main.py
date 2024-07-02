import numpy as np

def decomposer_en_facteurs_premiers(n):
    facteurs = []
    while n % 2 == 0:
        facteurs.append(2)
        n //= 2
    facteur = 3
    
    while facteur * facteur <= n:
        while n % facteur == 0:
            facteurs.append(facteur)
            n //= facteur
        facteur += 2
        
    if n > 2:
        facteurs.append(n)

    return facteurs

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def ppcm(a, b):
    return abs(a * b) // pgcd(a, b)

def is_prime_number(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Pas de solution réelle"
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b + np.sqrt(delta)) / (2*a)
        x2 = (-b - np.sqrt(delta)) / (2*a)
        return x1, x2

def degrees_to_radians(degrees):
    return np.deg2rad(degrees)

def radians_to_degrees(radians):
    return np.rad2deg(radians)

def sine(angle_radians):
    return np.sin(angle_radians)

def cosine(angle_radians):
    return np.cos(angle_radians)

def tangent(angle_radians):
    return np.tan(angle_radians)

def mean(data):
    return np.mean(data)

def median(data):
    return np.median(data)

def mode(data):
    values, counts = np.unique(data, return_counts=True)
    max_count_index = np.argmax(counts)
    return values[max_count_index]

def variance(data):
    return np.var(data)

def standard_deviation(data):
    return np.std(data)

def derivative(f, x, h=1e-7):
    return (f(x + h) - f(x - h)) / (2 * h)

def integral(f, a, b, n=1000):
    x = np.linspace(a, b, n)
    y = f(x)
    return np.trapz(y, x)

def area_of_circle(radius):
    return np.pi * radius**2

def circumference_of_circle(radius):
    return 2 * np.pi * radius

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_rectangle(length, width):
    return length * width

def volume_of_cube(side):
    return side**3

def volume_of_sphere(radius):
    return (4/3) * np.pi * radius**3

def factorial(n):
    return np.math.factorial(n)

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def solve_linear_system(A, b):
    return np.linalg.solve(A, b)

def matrix_determinant(A):
    return np.linalg.det(A)

def matrix_inverse(A):
    return np.linalg.inv(A)

def arc_sine(value):
    return np.arcsin(value)

def arc_cosine(value):
    return np.arccos(value)

def arc_tangent(value):
    return np.arctan(value)

def correlation_coefficient(x, y):
    return np.corrcoef(x, y)[0, 1]

def covariance(x, y):
    return np.cov(x, y)[0, 1]

def linear_regression(x, y):
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    return m, c

def area_of_trapezoid(a, b, h):
    return 0.5 * (a + b) * h

def area_of_parallelogram(base, height):
    return base * height

def volume_of_cylinder(radius, height):
    return np.pi * radius**2 * height

def volume_of_cone(radius, height):
    return (1/3) * np.pi * radius**2 * height

def second_derivative(f, x, h=1e-5):
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

def partial_derivative(f, var, point, h=1e-5):
    args = point[:]
    args[var] += h
    f_plus = f(*args)
    args[var] -= 2 * h
    f_minus = f(*args)
    return (f_plus - f_minus) / (2 * h)

def combinations(n, k):
    return np.math.comb(n, k)

def permutations(n, k):
    return np.math.perm(n, k)

def gcd_multiple(numbers):
    from functools import reduce
    return reduce(pgcd, numbers)

def lcm_multiple(numbers):
    from functools import reduce
    return reduce(ppcm, numbers)

# Transformations géométriques
def translate_point(point, translation_vector):
    return np.array(point) + np.array(translation_vector)

def rotate_point(point, angle_degrees, origin=(0, 0)):
    angle_radians = np.deg2rad(angle_degrees)
    ox, oy = origin
    px, py = point
    qx = ox + np.cos(angle_radians) * (px - ox) - np.sin(angle_radians) * (py - oy)
    qy = oy + np.sin(angle_radians) * (px - ox) + np.cos(angle_radians) * (py - oy)
    return qx, qy

def scale_point(point, scale_factor, origin=(0, 0)):
    ox, oy = origin
    px, py = point
    qx = ox + scale_factor * (px - ox)
    qy = oy + scale_factor * (py - oy)
    return qx, qy

# Statistiques avancées (suite)
def percentile(data, percentile_rank):
    return np.percentile(data, percentile_rank)

def skewness(data):
    from scipy.stats import skew
    return skew(data)

def kurtosis(data):
    from scipy.stats import kurtosis
    return kurtosis(data)

# Algorithmes numériques
def bisection_method(f, a, b, tol=1e-5):
    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit avoir des signes opposés aux points a et b")
    c = a
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return c

def newton_raphson_method(f, df, x0, tol=1e-5, max_iter=1000):
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Dérivée nulle. La méthode de Newton-Raphson échoue.")
        x = x - fx / dfx
    raise ValueError("Convergence non atteinte après le nombre maximum d'itérations")

# Mathématiques diverses
def harmonic_mean(data):
    from scipy.stats import hmean
    return hmean(data)

def geometric_mean(data):
    from scipy.stats import gmean
    return gmean(data)

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def is_perfect_square(n):
    return int(np.sqrt(n))**2 == n

def is_fibonacci_number(n):
    x1 = 5*n*n + 4
    x2 = 5*n*n - 4
    return is_perfect_square(x1) or is_perfect_square(x2)

if __name__ == "__main__":
    print("Facteurs premiers de 56:", decomposer_en_facteurs_premiers(56))
    print("PGCD de 48 et 18:", pgcd(48, 18))
    print("PPCM de 48 et 18:", ppcm(48, 18))
    print("Est-ce que 29 est un nombre premier?", is_prime_number(29))
    print("Solutions de l'équation quadratique 2x² + 4x - 6 = 0:", solve_quadratic(2, 4, -6))
    print("Sine de 90 degrés:", sine(degrees_to_radians(90)))
    print("Moyenne de [1, 2, 3, 4, 5]:", mean([1, 2, 3, 4, 5]))
    print("Volume d'une sphère de rayon 3:", volume_of_sphere(3))
    print("Factorial de 5:", factorial(5))
    print("Fibonacci des 10 premiers nombres:", fibonacci(10))
    print("Résolution du système linéaire Ax=b où A=[[3, 1], [1, 2]] et b=[9, 8]:", solve_linear_system(np.array([[3, 1], [1, 2]]), np.array([9, 8])))
    print("Déterminant de la matrice [[1, 2], [3, 4]]:", matrix_determinant(np.array([[1, 2], [3, 4]])))
    print("Inverse de la matrice [[1, 2], [3, 4]]:", matrix_inverse(np.array([[1, 2], [3, 4]])))
    print("Coefficient de corrélation entre [1, 2, 3] et [4, 5, 6]:", correlation_coefficient([1, 2, 3], [4, 5, 6]))
    print("Aire d'un trapèze avec bases 3 et 4 et hauteur 5:", area_of_trapezoid(3, 4, 5))
    print("Volume d'un cylindre avec rayon 3 et hauteur 5:", volume_of_cylinder(3, 5))
    print("Combinaisons de 5 éléments pris 3 à la fois:", combinations(5, 3))
    print("Permutations de 5 éléments pris 3 à la fois:", permutations(5, 3))
    print("PGCD de [48, 64, 80]:", gcd_multiple([48, 64, 80]))
    print("PPCM de [48, 64, 80]:", lcm_multiple([48, 64, 80]))
    print("Translation du point (1, 2) par le vecteur (3, 4):", translate_point((1, 2), (3, 4)))
    print("Rotation du point (1, 0) de 90 degrés autour de l'origine:", rotate_point((1, 0), 90))
    print("Mise à l'échelle du point (2, 3) par un facteur de 2 par rapport à l'origine:", scale_point((2, 3), 2))
    
    data = [1, 2, 2, 3, 4]
    print("90ème percentile de [1, 2, 2, 3, 4]:", percentile(data, 90))
    print("Asymétrie de [1, 2, 2, 3, 4]:", skewness(data))
    print("Kurtosis de [1, 2, 2, 3, 4]:", kurtosis(data))
    
    f = lambda x: x**3 - x - 2
    df = lambda x: 3*x**2 - 1
    print("Racine de l'équation x^3 - x - 2 = 0 par méthode de bissection:", bisection_method(f, 1, 2))
    print("Racine de l'équation x^3 - x - 2 = 0 par méthode de Newton-Raphson:", newton_raphson_method(f, df, 1))
    
    print("Moyenne harmonique de [1, 2, 4]:", harmonic_mean([1, 2, 4]))
    print("Moyenne géométrique de [1, 2, 4]:", geometric_mean([1, 2, 4]))
    print("Factoriel récursif de 5:", factorial_recursive(5))
    print("Est-ce que 16 est un carré parfait?", is_perfect_square(16))
    print("Est-ce que 21 est un nombre de Fibonacci?", is_fibonacci_number(21))
