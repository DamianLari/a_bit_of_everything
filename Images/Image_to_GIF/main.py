import os
from PIL import Image
import argparse

def images_to_gif(image_folder, output_gif_file, duration=100):
    images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
    images.sort()
    
    if not images:
        print("Aucune image trouvée dans le dossier spécifié.")
        return

    frames = [Image.open(os.path.join(image_folder, img)) for img in images]
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
