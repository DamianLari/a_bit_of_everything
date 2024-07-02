import cv2
import os

def images_to_video(image_folder, output_video_file, fps=30):
    # Récupère la liste des fichiers d'images et les trie
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images.sort()

    # Lit la première image pour obtenir les dimensions
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Définit le codec et crée l'objet VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Utilise le codec MPEG-4
    video = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    for image in images:
        img_path = os.path.join(image_folder, image)
        frame = cv2.imread(img_path)
        video.write(frame)

    # Libère l'objet VideoWriter
    video.release()

# Exemple d'utilisation
image_folder = "ImagesFolder"
output_video_file = "Outputvideo.mp4"
images_to_video(image_folder, output_video_file)
