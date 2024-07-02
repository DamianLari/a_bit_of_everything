
# Image to Video Converter

Ce script Python permet de créer une vidéo à partir d'un dossier contenant des images nommées de manière séquentielle.

## Prérequis

Assurez-vous d'avoir installé les bibliothèques Python nécessaires avant d'exécuter le script.

```bash
pip install opencv-python
```

## Utilisation

1. Clonez ce dépôt ou téléchargez le fichier `create_video_from_images.py`.

2. Placez vos images dans un dossier. Les images doivent être nommées de manière séquentielle, par exemple :
    ```
    image00000.png
    image00001.png
    image00002.png
    ...
    ```

3. Modifiez le script pour indiquer le chemin de votre dossier d'images et le chemin de sortie de la vidéo. Par exemple :
    ```python
    image_folder = "ImagesFolder"
    output_video_file = "Outputvideo.mp4"
    ```

4. Exécutez le script en utilisant la commande suivante :
    ```bash
    python create_video_from_images.py
    ```

## Code

Voici le script complet :

```python
import cv2
import os

def images_to_video(image_folder, output_video_file, fps=30):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    video.release()

image_folder = "chemin/vers/dossier_images"
output_video_file = "chemin/vers/sortie_video.mp4"
images_to_video(image_folder, output_video_file)
```

## Paramètres

- `image_folder`: Chemin vers le dossier contenant les images.
- `output_video_file`: Chemin où la vidéo générée sera sauvegardée.
- `fps`: (Optionnel) Images par seconde pour la vidéo (par défaut: 30).

