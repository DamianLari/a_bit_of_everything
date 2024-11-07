import cv2
import os
import argparse

CODECS = {
    "mp4": 'mp4v',   
    "mkv": 'X264',   
    "avi": 'XVID',   
    "mov": 'mp4v',   
    "flv": 'FLV1',   
    "wmv": 'WMV2',   
    "webm": 'VP80',  
    "ogg": 'THEO'    
}

def images_to_video(image_folder, output_video_file, fps):
    output_extension = output_video_file.split('.')[-1].lower()
    if output_extension not in CODECS:
        print(f"Format de sortie '{output_extension}' non valide. Veuillez utiliser l'un des formats suivants : {', '.join(CODECS.keys())}")
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
