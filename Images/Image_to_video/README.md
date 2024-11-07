# Image to Video Converter

Ce script Python permet de créer une vidéo à partir d'un dossier contenant des images nommées de manière séquentielle, en choisissant le nombre d'images par seconde (fps) et le format de la vidéo.

## Prérequis

Assurez-vous d'avoir installé les bibliothèques Python nécessaires avant d'exécuter le script.

```bash
pip install opencv-python
```

## Utilisation

1. Clonez ce dépôt ou téléchargez le fichier `main.py`.

2. Placez vos images dans un dossier. Les images doivent être nommées de manière séquentielle, par exemple :
    ```
    image00000.png
    image00001.png
    image00002.png
    ...
    ```

3. Exécutez le script en utilisant la commande suivante, en spécifiant le dossier d'images, le fichier de sortie (avec son extension) et, si besoin, les options supplémentaires :
    ```bash
    python main.py <dossier_images> <fichier_video_sortie> --fps <nombre_fps>
    ```

    **Exemple** :
    ```bash
    python main.py ImagesFolder OutputVideo.mkv --fps 24
    ```

### Formats de sortie pris en charge
Le script prend en charge les formats vidéo suivants : `mp4`, `mkv`, `avi`, `mov`, `flv`, `wmv`, `webm`, `ogg`. Assurez-vous d'indiquer une extension de fichier valide pour le fichier vidéo de sortie. Si un format non supporté est choisi, le script affichera un message d'erreur.

## Code

Voici le script complet :

```python
import cv2
import os
import argparse

# Dictionnaire des codecs vidéo par format
CODECS = {
    "mp4": 'mp4v',   # Codec pour MP4
    "mkv": 'X264',   # Codec pour MKV
    "avi": 'XVID',   # Codec pour AVI
    "mov": 'mp4v',   # Codec pour MOV
    "flv": 'FLV1',   # Codec pour FLV
    "wmv": 'WMV2',   # Codec pour WMV
    "webm": 'VP80',  # Codec pour WEBM
    "ogg": 'THEO'    # Codec pour OGG
}

def images_to_video(image_folder, output_video_file, fps):
    output_extension = output_video_file.split('.')[-1].lower()
    if output_extension not in CODECS:
        print(f"Format de sortie '{output_extension}' non valide. Utilisez un des formats : {', '.join(CODECS.keys())}")
        return

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()
    if not images:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*CODECS[output_extension])
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    video.release()
    print(f"Vidéo créée avec succès : {output_video_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Créer une vidéo à partir d'images")
    parser.add_argument("image_folder", type=str, help="Le dossier contenant les images")
    parser.add_argument("output_video_file", type=str, help="Le fichier vidéo de sortie")
    parser.add_argument("--fps", type=int, default=30, help="Nombre d'images par seconde (fps) pour la vidéo")

    args = parser.parse_args()
    images_to_video(args.image_folder, args.output_video_file, args.fps)
```

## Paramètres

- `image_folder`: Chemin vers le dossier contenant les images.
- `output_video_file`: Chemin et nom du fichier de sortie de la vidéo avec son extension.
- `fps`: (Optionnel) Nombre d'images par seconde pour la vidéo (par défaut : 30).