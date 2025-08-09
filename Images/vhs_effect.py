import cv2
import numpy as np
import random
import subprocess
import os

def add_vhs_effect(frame, frame_count, fps):
    height, width = frame.shape[:2]

    # === Bruit (grain) ===
    noise = np.random.normal(0, 6, (height, width, 1)).astype(np.int16)
    noise = np.repeat(noise, 3, axis=2)
    frame_int = frame.astype(np.int16)
    noisy_frame = np.clip(frame_int + noise, 0, 255).astype(np.uint8)

    # === Scanlines ===
    for y in range(0, height, 3):
        noisy_frame[y:y+1, :] = (noisy_frame[y:y+1, :] * 0.5).astype(np.uint8)

    # === Déphasage RGB ===
    b, g, r = cv2.split(noisy_frame)
    b = np.roll(b, 1, axis=1)
    r = np.roll(r, -1, axis=1)
    shifted = cv2.merge((b, g, r))

    # === Pas de distorsion ===
    distorted = shifted.copy()

    # === Flou léger ===
    blurred = cv2.GaussianBlur(distorted, (3, 3), 0)

    # === Timestamp vidéo réel ===
    seconds = frame_count / fps
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    timestamp = f"REC  {h:02d}:{m:02d}:{s:02d}"

    cv2.putText(
        blurred,
        timestamp,
        (20, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 255),  # Jaune VHS
        1,
        cv2.LINE_AA
    )

    return blurred




def process_video(input_path, temp_output_path, final_output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Erreur lors de l'ouverture de la vidéo.")
        return

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out    = cv2.VideoWriter(temp_output_path, fourcc, fps, (width, height))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        vhs_frame = add_vhs_effect(frame, frame_count)
        out.write(vhs_frame)
        frame_count += 1

    cap.release()
    out.release()
    print("Vidéo modifiée sans audio créée :", temp_output_path)

    # === Ajout du son original avec ffmpeg ===
    try:
        cmd = [
            "ffmpeg", "-y",  # overwrite if exists
            "-i", temp_output_path,
            "-i", input_path,
            "-c", "copy",
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-shortest",
            final_output_path
        ]
        subprocess.run(cmd, check=True)
        print("Vidéo finale avec son :", final_output_path)
    except subprocess.CalledProcessError as e:
        print("Erreur lors de la fusion avec le son :", e)


if __name__ == "__main__":
    input_video = "input.mp4"
    temp_video = "output_vhs_temp.mp4"     # Vidéo sans son
    final_video = "output_vhs.mp4"         # Vidéo avec son
    process_video(input_video, temp_video, final_video)

    # Nettoyage du fichier temporaire
    if os.path.exists(temp_video):
        os.remove(temp_video)
