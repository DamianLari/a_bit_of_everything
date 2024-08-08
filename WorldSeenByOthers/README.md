# Simulateur de Vision des Couleurs et de Vision Animale

Ce script Python utilise OpenCV pour simuler différents types de déficiences visuelles humaines (comme le daltonisme) ainsi que la perception visuelle de certains animaux. Il permet de transformer une image, une vidéo ou un flux de caméra en une représentation approximative de la façon dont certaines espèces voient le monde.

## Fonctionnalités

- **Simuler la vision humaine avec des déficiences visuelles** : Deutéranopie, Protanopie, Tritanopie.
- **Simuler la vision animale** : Perception visuelle des chiens, chats, oiseaux, requins et serpents.
- **Entrées multiples** : Le script peut traiter une image, une vidéo ou un flux de caméra en temps réel.

## Prérequis

Avant d'utiliser ce script, vous devez avoir installé ainsi les bibliothèques suivantes :
- OpenCV : Pour le traitement des images et vidéos.
- NumPy : Pour la manipulation des matrices.

Vous pouvez installer ces bibliothèques avec pip :

```bash
pip install opencv-python numpy
```

## Utilisation

1. **Choisir la source** :
   - Modifiez la variable `source_type` dans le script pour choisir entre `'image'`, `'video'` ou `'camera'`.
   - Si vous choisissez `'image'`, assurez-vous de spécifier le chemin de l'image avec `cv2.imread('path_to_image.jpg')`.
   - Pour `'video'`, remplacez `'path_to_video.mp4'` par le chemin de votre vidéo.
   - Pour `'camera'`, le script utilisera par défaut la caméra connectée à votre machine.

2. **Choisir le type de vision** :
   - Modifiez la variable `vision_type` pour sélectionner le type de vision que vous souhaitez simuler. Les options disponibles sont :
     - `'normal'` : Vision humaine standard.
     - `'deuteranopia'` : Déficience de la perception du vert.
     - `'protanopia'` : Déficience de la perception du rouge.
     - `'tritanopia'` : Déficience de la perception du bleu.
     - `'dog'` : Vision canine, limitée dans la perception des couleurs.
     - `'cat'` : Vision féline, adaptée à la vision nocturne.
     - `'bird'` : Vision aviaire, avec des couleurs plus vives.
     - `'shark'` : Vision de haute contraste, adaptée à la chasse sous-marine.
     - `'snake'` : Vision des serpents, plus axée sur les contrastes que sur les couleurs.

3. **Exécuter le script** :
   - Une fois les paramètres configurés, exécutez le script via Python :

   ```bash
   python simulate_color_vision.py
   ```

4. **Arrêter le script** :
   - Pour arrêter le script pendant le traitement de la vidéo ou du flux de la caméra, appuyez sur la touche `q`.

## Exemple de Commande

```bash
python main.py
```

Dans cet exemple, le script transformera la vidéo ou l'image spécifiée en simulant la vision du type défini dans `vision_type`.

## Avertissements

- Les simulations de vision animale sont des approximations basées sur des descriptions générales et des études théoriques. Elles peuvent ne pas refléter précisément la vision de chaque espèce.
