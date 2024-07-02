# Comparaison d'Images et Mise en Évidence des Différences

Ce projet contient un script Python pour comparer deux images, calculer leurs différences et mettre en évidence ces différences à l'aide de seuils binaires.

## Table des Matières
1. [Pré-requis](#pré-requis)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
4. [Exemples](#exemples)
5. [Notes](#notes)

## Pré-requis

- Python 3.x
- `opencv-python` pour la manipulation des images
- `numpy` pour les opérations mathématiques
- `matplotlib` pour la visualisation

## Installation

Installez les dépendances nécessaires en utilisant pip :

```bash
pip install opencv-python numpy matplotlib
```

## Utilisation

Le script compare deux images, calcule leurs différences et affiche les images originales, la différence et les différences mises en évidence par un seuil binaire.

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

if image1.shape != image2.shape:
    print("Les images doivent avoir la même taille et les mêmes dimensions.")
    exit()

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Soustraction des images
diff_image = cv2.absdiff(gray_image1, gray_image2)

# Seuil pour mettre en évidence les différences
_, thresh_image = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)

# Affichage des images
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)), plt.title('Image 1')
plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)), plt.title('Image 2')
plt.subplot(2, 2, 3), plt.imshow(diff_image, cmap='gray'), plt.title('Différence')
plt.subplot(2, 2, 4), plt.imshow(thresh_image, cmap='gray'), plt.title('Différences Seuil')
plt.show()
```

## Exemples

Pour utiliser ce script, placez deux images (`image1.jpg` et `image2.jpg`) dans le même répertoire que le script, puis exécutez-le. Le script affichera les deux images originales, la différence en niveaux de gris et les différences mises en évidence par un seuil binaire.

```bash
python compare_images.py
```

## Notes

- Les images doivent avoir la même taille et les mêmes dimensions. Si ce n'est pas le cas, le script affichera un message d'erreur et se terminera.
- Le seuil de différence est fixé à 30. Vous pouvez ajuster ce seuil en modifiant la valeur dans la fonction `cv2.threshold`.
