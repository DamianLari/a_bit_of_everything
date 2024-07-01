import cv2
import time
from TB_calibration import CalibrationProvider

#========================Exemple d'utilisation========================#
# Paramètres pour la calibration
number_columns = 7  # Nombre de colonnes du damier -1 (car les coins sont dans les intersections)
number_rows = 8     # Nombre de lignes du damier -1 (car les coins sont dans les intersections)
# Un damier de dimension 7x8 (carrés) a 6x7 intersections

calibration_path = "calibration_file.json"  # Chemin du fichier où sauvegarder les données de calibration

max_image = 300     # Nombre maximal d'images à capturer pour la calibration
chessboard_wanted = 200  # Nombre de damiers à détecter pour une calibration réussie

# Initialisation de la capture vidéo
capture = cv2.VideoCapture(0)        
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Réglage de la largeur de l'image, ajustable selon votre caméra
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Réglage de la hauteur de l'image, ajustable également

# Listes pour stocker les points d'image (détections de coins) et les points objets (références 3D)
point_image = []
point_objet = []

# Création d'une instance de CalibrationProvider avec les dimensions du damier
calibration_provider = CalibrationProvider(number_columns, number_rows)

# Boucle de capture d'images pour la calibration
for image in range(max_image):
    ret, frame = capture.read()  # Lecture d'une image de la caméra
    calibration_provider.simulation(frame)  # Simulation pour visualiser les détections de damier
    print("image traitée:", image)

    # Recherche des coins du damier dans l'image et mise à jour des listes de points
    corners, point_objet = calibration_provider.find_and_update_chessboard_corners(frame, point_objet)

    # Ajout des coins détectés à la liste des points d'image, si présents
    if corners is not None:
        point_image.append(corners)

        # Vérification si le nombre de damiers détectés atteint le seuil souhaité
        if len(point_image) == chessboard_wanted:
            break

capture.release()  # Fin de la capture vidéo   

# Processus de Calibration et Enregistrement des Données
# Vérification si suffisamment de damiers ont été détectés pour une calibration fiable
if len(point_objet) >= chessboard_wanted and len(point_image) >= chessboard_wanted:
    print("Nombre de damiers détectés:", len(point_image))
    start_time = time.time()

    # Calibration de la caméra et enregistrement des données de calibration
    mtx, dist, rvecs, tvecs = calibration_provider.perform_camera_calibration_and_save(point_objet, point_image, frame.shape[1::-1], calibration_path)
    elapsed_time = time.time() - start_time
    print(f"Temps de calcul :{elapsed_time} secondes")
    print("mtx:", mtx)  # Matrice de calibration de la caméra
    print("dist:", dist)  # Coefficients de distortion

    # Calcul de l'erreur de reprojection
    error = calibration_provider.calculate_reprojection_error(point_objet, point_image, rvecs, tvecs, mtx, dist)
    print(f"Erreur de reprojection moyenne: {error} pixels")

    # Calcule et visualisation de l'erreur de reprojection
    mean_error, error_image = calibration_provider.calculate_and_visualize_reprojection_error(point_objet, point_image, rvecs, tvecs, mtx, dist, [480, 640])
    print(f"Erreur de reprojection moyenne: {mean_error} pixels")
    cv2.imwrite("reprojection_error_image.png", error_image)  # Sauvegarde de l'image de l'erreur de reprojection

else:
    # Message en cas de nombre insuffisant de détections de damier
    print(f"Nombre de damiers détectés inférieur au nombre demandé: {len(point_image)}différence:{chessboard_wanted-len(point_image)}")