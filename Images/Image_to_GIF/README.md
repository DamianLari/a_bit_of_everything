# Image to GIF Converter

Ce script Python permet de créer un GIF animé à partir d'un dossier contenant des images nommées de manière séquentielle.

## Prérequis

Assurez-vous d'avoir installé la bibliothèque Python `Pillow` avant d'exécuter le script.

```bash
pip install pillow
```

## Utilisation

1. Clonez ce dépôt ou téléchargez le fichier `main.py`.

2. Placez vos images dans un dossier. Les images doivent être nommées de manière séquentielle pour garantir l'ordre correct dans le GIF, par exemple :
    ```
    image00000.png
    image00001.png
    image00002.png
    ...
    ```

3. Exécutez le script en utilisant la commande suivante, en spécifiant le dossier d'images et le nom du fichier GIF de sortie, et éventuellement la durée d'affichage de chaque image (en millisecondes) :
    ```bash
    python main.py <dossier_images> <fichier_gif_sortie> --duration <durée_par_image>
    ```

    **Exemple** :
    ```bash
    python main.py ImagesFolder OutputGif.gif --duration 200
    ```

## Code

Voici le script complet :

```python
import os
from PIL import Image
import argparse

def images_to_gif(image_folder, output_gif_file, duration=100):
    # Récupère la liste des fichiers d'images et les trie
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()
    
    # Vérifie qu'il y a au moins une image dans le dossier
    if not images:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    # Charge les images et les ajoute à une liste
    frames = [Image.open(os.path.join(image_folder, img)) for img in images]
    
    # Crée le GIF avec la liste d'images
    frames[0].save(
        output_gif_file, 
        save_all=True, 
        append_images=frames[1:], 
        duration=duration, 
        loop=0
    )

    print(f"GIF créé avec succès : {output_gif_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Créer un GIF animé à partir d'images")
    parser.add_argument("image_folder", type=str, help="Le dossier contenant les images")
    parser.add_argument("output_gif_file", type=str, help="Le fichier GIF de sortie")
    parser.add_argument("--duration", type=int, default=100, help="Durée de chaque image en millisecondes")

    args = parser.parse_args()
    images_to_gif(args.image_folder, args.output_gif_file, args.duration)
```

## Paramètres

- `image_folder`: Chemin vers le dossier contenant les images.
- `output_gif_file`: Chemin et nom du fichier de sortie du GIF.
- `duration`: (Optionnel) Durée d'affichage de chaque image en millisecondes (par défaut : 100 ms). 

## Note

Les images acceptées pour ce script doivent être au format `.png`, `.jpg` ou `.jpeg`. Si les images ne sont pas dans l'ordre désiré, renommez-les pour garantir une séquence correcte dans le GIF.