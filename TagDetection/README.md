# Détection de Marqueurs ArUco et AprilTag avec OpenCV

Ce script implémente un système de détection et de suivi des marqueurs ArUco et AprilTag en utilisant OpenCV et la bibliothèque AprilTag. Il est conçu pour traiter les images et détecter la position et l'orientation des marqueurs dans l'espace, utile dans des domaines comme la robotique et la réalité augmentée.

## Fonctionnalités

- Détection des marqueurs ArUco et AprilTag dans les images.
- Calcul de la pose (position et orientation) des marqueurs dans l'espace.
- Prise en charge de plusieurs configurations de tags et de caméras.
- Calcul et visualisation des erreurs de positionnement et d'orientation.

## Prérequis

- Python
- OpenCV
- NumPy
- SciPy
- AprilTag (bibliothèque)

## Utilisation

1. **Configuration de la Calibration** : Configurez les paramètres de calibration de la caméra, y compris la matrice de calibration et les coefficients de distorsion.
2. **Détection des Marqueurs** : Utilisez la méthode `detect_marker` pour détecter les marqueurs ArUco ou AprilTag dans une image.
3. **Calcul de la Pose** : Après la détection, calculez la pose des marqueurs en utilisant les méthodes `calculate_positions_in_world_frame` ou `calculate_positions_in_camera_frame`.
4. **Visualisation et Analyse** : Analysez les résultats obtenus pour les positions et les orientations des marqueurs, et visualisez les erreurs potentielles.

## Description des Méthodes du Code

### Classe `TagPoseProvider`
Gère la détection des marqueurs et le calcul de leur pose.

#### Méthodes
- `set_calibration_params(mtx, dist)`: Définit les paramètres de calibration de la caméra.
- `detect_marker(image, tag_type, tag_size, tag_dict)`: Détecte les marqueurs spécifiés dans une image.

### Classe `TagConfig`
Gère la configuration des marqueurs.

#### Méthodes
- `set_tag_params(tag_type, tag_size, tag_dict)`: Définit les paramètres d'un marqueur spécifique.

### Classe `CameraConfig`
Gère la configuration des caméras.

#### Méthodes
- `set_calibration_params(mtx, dist)`: Définit les paramètres de calibration d'une caméra spécifique.

### Classe `TagDetection`
Intègre les configurations des tags et des caméras pour la détection.

#### Méthodes
- `detector_callback()`: Méthode principale pour la détection des marqueurs à partir des images fournies par les caméras configurées.

## Exemple d'Utilisation

