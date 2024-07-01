from TB_tag_detection import TagPoseProvider, CameraConfig, TagConfig, TagDetection
import cv2
import os

#========================Exemple d'utilisation basique========================#

# Chemin vers le fichier contenant les données de calibration de la caméra
calibration_file = "calibration_data.json"

# Crée une instance de TagPoseProvider, qui gère la détection des tags et les calculs de pose
tag_detection_provider = TagPoseProvider()

# Charge les données de calibration de la caméra depuis un fichier JSON
# et définit les paramètres de calibration pour le fournisseur de détection
calib_data = tag_detection_provider.load_calib_data(calibration_file)
tag_detection_provider.set_calibration_params(*calib_data)

# Initialisation de la capture vidéo avec OpenCV (pour tu utilisation avec une caméra, sinon, utiliser une autre source tel qu'une image ou une vidéo)
capture = cv2.VideoCapture(0)        
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Largeur de l'image
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # Hauteur de l'image
ret, frame = capture.read()# Lit la première image de la vidéo

# Détecte les marqueurs AprilTag dans l'image capturée
# Les paramètres incluent l'image, le type de tag ('apriltag'), la taille des tags et le dictionnaire de tags
corners, ids, rvecs, tvecs = tag_detection_provider.detect_marker(frame, 'apriltag', 0.103, 'tag36h11')

# Vérifie si des marqueurs ont été détectés dans l'image
if ids is not None:
    # Calcule les positions des marqueurs Voir la documentation de la fonction pour plus de détail. Voir aussi la mehtode "calculate_positions_in_camera_frame" (dépend de votre besoin)
    # Retourne les identifiants des tags, les vecteurs de rotation et de translation
    ids, rota, transla = tag_detection_provider.calculate_positions_in_world_frame(ids, rvecs, tvecs)
    
    # Affiche les identifiants des marqueurs et leurs positions et orientations respectives
    for i in range(len(ids)):
        print(f"Le tag {ids[i]} est à la position {transla[i]} et à l'orientation {rota[i]}")

    # Option pour afficher l'image avec les marqueurs détectés
    # Décommentez la ligne suivante pour visualiser l'image avec les marqueurs superposés
    # cv2.imshow("image with tag", frame)



#========================Exemple d'utilisation plus poussé (en utilisant plusieurs caméra et tag) EN COURS DE FINALISATION ========================#




def simulate_robot(camera_config,tag_config):
    tag_detection_provider.set_calibration_params(*camera_config.get_calibration_params())

    image_path = camera_config.get_image_folder()
    file_list = os.listdir(image_path)
    image_list = [file for file in file_list if file.endswith(".png")]

    for img in image_list:

        cv_image = cv2.imread(os.path.join(image_path, img))
        
        corners, ids, rvecs, tvecs = tag_detection_provider.detect_marker(cv_image, *tag_config.get_tag_params()) # Exemple de paramètres
        
        if ids is not None:
            # Calcule les positions des marqueurs dans le cadre de référence mondial
            ids, rota, transla = tag_detection_provider.calculate_positions_in_world_frame(ids, rvecs, tvecs)
            tag_config.set_tag_id(ids)

            # Enregitre les positions et orientations du marqueur. 
            # Peut être utilisé avec des données réelles afin de les comparer avec les données calculées
            # Peut aussi être utilisé pour enregistrer les données du tag calculées par le robot afin de les utiliser dans la suite du script.
            # Remarque : Cela peut être une liste de positions comme une position unique. Cela dépendra de l'utilisation que vous en fait.
            # Attention : Si vous utilisez une liste de positions, il faudra faire attention à l'ordre des positions dans la liste.
            #             Vous définissez les données du tag donc c'est à vous de voir dans quel repère vous souhaitez les définir.
            tag_config.set_tag_rvec(rota)
            tag_config.set_tag_tvec(transla)
            
            print(tag_config.get_tag_id())
            print(tag_config.get_tag_rvec())
            print(tag_config.get_tag_tvec())
           


tag_list = [
    {'type': 'apriltag', 'size': 0.103, 'dict': 'tag36h11'},
    {'type': 'aruco', 'size': 0.100, 'dict': 'DICT_4X4_200'}
]

camera_list = [
    {'name':'camera1', 'calibration_file': 'calibration_data1.json', 'images_folder': 'camera1_images'},
    {'name':'camera2', 'calibration_file': 'calibration_data2.json', 'images_folder': 'camera2_images'},
    {'name':'camera3', 'calibration_file': 'calibration_data3.json', 'images_folder': 'camera3_images'}
]

tag_detection_provider = TagPoseProvider()

# Cette fonction charge les paramètres de calibration de toutes les caméras et de tous les tags
# L'utilisation de cette fonction est optionnelle. Elle permet de charger les paramètres de calibration de toutes les caméras et de tous les tags en une seule fois. Vous pouvez aussi charger les paramètres de calibration de chaque caméra et de chaque tag séparément.
# Elle retourne deux dictionnaires : un pour les tags et un pour les caméras
# Atention : Les noms des tags et des caméras doivent être uniques  
#            Les informations concernant les tag sont celles de base (type, taille, dictionnaire). Pour les modifier, il faudra le faire après l'appel de la fonction via les fonctions set_tag_params. Pour ajouter des paramètres (id,rvec,tvec), il faudra le faire via l'appel de des methodes dédiées.
#             
tag_config, camera_config = tag_detection_provider.load_global_config(tag_list, camera_list)

for camera_config in tag_detection_provider.camera_config:
    # Ici nous utilisons la fonction simulate_robot pour simuler plusieurs caméras et un seul tag.
    simulate_robot(camera_config, tag_detection_provider.tag_config[0])