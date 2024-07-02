# Transformation 3D et Visualisation des Erreurs

Ce projet contient une classe pour calculer les transformations moyennes en 3D et visualiser les erreurs de transformation en utilisant des graphiques 2D et 3D.

## Table des Matières
1. [Pré-requis](#pré-requis)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
    - [Calcul de la Transformation Moyenne en 3D](#calcul-de-la-transformation-moyenne-en-3d)
    - [Calcul de la Transformation Moyenne](#calcul-de-la-transformation-moyenne)
    - [Visualisation des Erreurs de Transformation](#visualisation-des-erreurs-de-transformation)
4. [Exemples](#exemples)

## Pré-requis

- Python 3.x
- `numpy` pour les calculs mathématiques
- `matplotlib` pour la visualisation
- `scipy` pour les transformations spatiales

## Installation

Installez les dépendances nécessaires en utilisant pip :

```bash
pip install numpy matplotlib scipy
```

## Utilisation

### Calcul de la Transformation Moyenne en 3D

La méthode `average_transform_3d_graph` calcule la transformation moyenne des matrices de transformation 3D et crée une animation de la position moyenne.

```python
def average_transform_3d_graph(self):
    ...
    return mean_transform
```

### Calcul de la Transformation Moyenne

La méthode `average_transform_graph` calcule la transformation moyenne et génère des graphiques 2D pour les composantes de translation et de rotation.

```python
def average_transform_graph(self):
    ...
    return mean_transform
```

### Visualisation des Erreurs de Transformation

La méthode `transformation_error_graph` calcule et visualise les erreurs de transformation par rapport à une transformation de référence.

```python
def transformation_error_graph(self, ref_transform, type_graph):
    ...
    return mean_translation_error, mean_rotation_error
```

## Exemples

Voici des exemples d'utilisation de ces méthodes :

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
from transformation import transformation

# Exemple de données
all_T_base_to_tag = [np.eye(4) for _ in range(10)]  # Remplacer par vos données de transformation

# Création de l'objet transformation
trans = transformation()
trans.all_T_base_to_tag = all_T_base_to_tag

# Calcul de la transformation moyenne en 3D
mean_transform_3d = trans.average_transform_3d_graph()

# Calcul de la transformation moyenne
mean_transform = trans.average_transform_graph()

# Visualisation des erreurs de transformation
ref_transform = np.eye(4)  # Remplacer par votre transformation de référence
mean_translation_error, mean_rotation_error = trans.transformation_error_graph(ref_transform, 'type_graph')
```