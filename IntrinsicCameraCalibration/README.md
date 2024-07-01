





# Calibration de Caméra avec OpenCV

Ce script fournit une méthode complète pour calibrer une caméra en utilisant OpenCV en Python. Il détecte les coins d'un damier dans des images pour calculer la matrice de calibration de la caméra et les coefficients de distortion.

## Fonctionnalités

- Calibration de caméra en temps réel ou à partir d'images/vidéos statiques.
- Détecte les coins d'un damier dans des images pour la calibration.
- Calcul et visualisation de l'erreur de reprojection.
- Enregistrement des données de calibration dans un fichier JSON.

## Prérequis

- Python
- OpenCV
- NumPy
- SciPy


## Utilisation

1. **Configuration** : Définissez les paramètres de calibration, notamment les dimensions du damier (nombre de colonnes et de lignes), le chemin du fichier de calibration, et le nombre de damiers à détecter.

2. **Capture d'Images** : Le script peut être configuré pour capturer des images en temps réel à partir d'une caméra, à partir d'un dossier d'images, ou à partir d'un fichier vidéo.

3. **Détection des Coins du Damier** : Utilisez la méthode `find_and_update_chessboard_corners` pour détecter et raffiner les coins du damier dans chaque image capturée.

4. **Calibration de la Caméra** : Une fois le nombre souhaité de damiers détectés, utilisez la méthode `perform_camera_calibration_and_save` pour effectuer la calibration et enregistrer les résultats dans un fichier JSON.

5. **Calcul de l'Erreur de Reprojection** : La méthode `calculate_reprojection_error` permet de calculer l'erreur de reprojection, qui est un indicateur de la précision de la calibration.

6. **Visualisation de l'Erreur** : Utilisez la méthode `calculate_and_visualize_reprojection_error` pour visualiser l'erreur de reprojection sur les images.


## Description des méthodes du code

- `__init__(colonnes, lignes)` : Initialise la classe avec les dimensions du damier (nombre de colonnes et de lignes).

- `find_and_update_chessboard_corners(img, pointsobj)` : Détecte les coins du damier dans une image donnée (`img`) et met à jour la liste des points objets (`pointsobj`). Retourne les coins raffinés et la liste mise à jour.

- `perform_camera_calibration_and_save(pointsobj, imgpoints, img_size, calibration_file)` : Effectue la calibration de la caméra en utilisant les points objets (`pointsobj`) et les points d'image (`imgpoints`), puis enregistre les données de calibration dans un fichier JSON (`calibration_file`).

- `check_chessboard(img)` : Vérifie si un damier est détecté dans l'image donnée (`img`). Retourne un booléen indiquant si un damier est détecté, les coins détectés et l'historique de détection.

- `simulation(frame)` : Simule la détection de damier dans une image (`frame`) et ajoute une bordure colorée basée sur le taux de détection. Plus la bordure et moins le damier est détécté,plus la bordure est verte et plus le damier est présent sur les images analysées.

- `calculate_reprojection_error(objpoints, imgpoints, rvecs, tvecs, mtx, dist)` : Calcule l'erreur de reprojection pour la calibration de la caméra.

- `calculate_and_visualize_reprojection_error(objpoints, imgpoints, rvecs, tvecs, mtx, dist, image_shape)` : Calcule et visualise l'erreur de reprojection pour la calibration de la caméra.

- `save_data(calib_folder, mtx, dist, erreur_projection)` : Enregistre les données de calibration dans un fichier texte.



