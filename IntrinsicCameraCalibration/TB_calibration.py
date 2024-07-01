import numpy as np
import cv2
import json
import codecs
from collections import deque
import os
import scipy.interpolate
import time

class CalibrationProvider:
    #==========================================
    # Cette classe permet de fournir la matrice de calibration et les coefficients de distortion
    #==========================================
    def __init__(self, colonnes, lignes):
        """
        Initialise le CalibrationProvider avec les dimensions spécifiées du damier.

        Args:
            colonnes (int): Nombre de colonnes du damier.
            lignes (int): Nombre de lignes du damier.
        """
        
        self.cols = colonnes 
        self.rows = lignes
       
        
        self.objp = np.zeros((self.rows * self.cols, 3), np.float32)
        self.objp[:,:2] = np.mgrid[0:self.cols, 0:self.rows].T.reshape(-1, 2) #* self.taille_case
        self.criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        
        self.detection_history = deque(maxlen=10)

  
    def find_and_update_chessboard_corners(self,img,pointsobj):
        """
        Trouve et raffine les coins du damier dans une image donnée.
        
        Args:
            img (numpy.array): Image dans laquelle chercher les coins du damier.
            pointsobj (list): Liste actuelle de points objets qui sera mise à jour.

        Returns:
            tuple: Un tuple contenant les coins raffinés du damier (numpy.array) 
                   et la liste mise à jour des points objets (list). Renvoie None 
                   et la liste des points objets inchangée si aucun damier n'est détecté.
        """
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        ret, corners = cv2.findChessboardCorners(gray, (self.cols,self.rows), None)
        corners2 = []
        if ret == True:    
            pointsobj.append(self.objp)
            # Refine the corners of the detected corners
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),self.criteria)
            return corners2, pointsobj
        else: 
            return None,pointsobj

        
   
    def perform_camera_calibration_and_save(self,pointsobj,imgpoints,img_size,calibration_file):
        """
        Effectue la calibration de la caméra en utilisant les points objets et les points d'image, 
        et enregistre les données de calibration dans un fichier JSON.

        @param pointsobj: Liste de points objets.
        @type pointsobj: list

        @param imgpoints: Liste de points d'image.
        @type imgpoints: list

        @param img_size: Taille de l'image (largeur, hauteur).
        @type img_size: tuple

        @param calibration_file: Chemin du fichier pour enregistrer les données de calibration.
        @type calibration_file: str

        @return: Un tuple contenant la matrice de calibration de la caméra (numpy.array), 
                les coefficients de distortion (numpy.array), les vecteurs de rotation (list) 
                et les vecteurs de translation (list).
        @rtype: tuple

        @note: Cette fonction nécessite OpenCV pour la calibration de la caméra.
        @attention: Assurez-vous que les points objets et les points d'image sont correctement alignés.
        """
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(pointsobj, imgpoints, img_size,None,None)
        data = {"mtx":mtx.tolist(),"dist":dist.tolist()}

        os.makedirs(os.path.dirname(calibration_file), exist_ok=True)
        json.dump(data, codecs.open(calibration_file, 'w', encoding='utf-8'), 
        separators=(',', ':'), 
        sort_keys=True, 
        indent=4)

        print("Donnée enregistrée dans:", calibration_file)
        
        return mtx , dist, rvecs, tvecs
    
    
    def check_chessboard(self, img):
        """
        Vérifie si un damier est détecté dans l'image donnée.

        Args:
            img (numpy.array): Image dans laquelle chercher le damier.

        Returns:
            tuple: Un tuple contenant un booléen indiquant si un damier est détecté,
                   les coins détectés (numpy.array) et l'historique de détection (deque).
        """
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (self.cols,self.rows), None)
        self.detection_history.append(ret)
        return ret ,corners, self.detection_history
    
    
    def simulation(self,frame):
        """
        Simule la détection de damier dans une image et ajoute une bordure colorée basée 
        sur le taux de détection.

        Args:
            frame (numpy.array): Image à traiter pour la simulation.

        Affiche l'image traitée avec une bordure colorée indiquant le taux de détection.
        """
        is_detected = self.check_chessboard(frame)

        # Calculate the average detection rate
        detection_rate = sum(self.detection_history) / len(self.detection_history)

        # Determine the border color based on the detection rate
        red = int((1 - detection_rate) * 255)
        green = int(detection_rate * 255)
        color = (0, green, red) 

        # Add a border to the image
        bordered_frame = cv2.copyMakeBorder(frame, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=color)

        cv2.imshow('frame', bordered_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def calculate_reprojection_error(self, objpoints, imgpoints, rvecs, tvecs, mtx, dist):
        """
        Calcule l'erreur de reprojection pour la calibration de la caméra.

        Args:
            objpoints (list): Liste de points objets.
            imgpoints (list): Liste de points d'image.
            rvecs (list): Vecteurs de rotation estimés par la calibration.
            tvecs (list): Vecteurs de translation estimés par la calibration.
            mtx (numpy.array): Matrice de calibration de la caméra.
            dist (numpy.array): Coefficients de distortion.

        Returns:
            float: Erreur de reprojection moyenne.
        """
        total_error = 0
        for i in range(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
            total_error += error
        return total_error / len(objpoints)
    

    def calculate_and_visualize_reprojection_error(self, objpoints, imgpoints, rvecs, tvecs, mtx, dist, image_shape):
        """
        Calcule et visualise l'erreur de reprojection pour la calibration de la caméra.

        Args:
            objpoints (list): Liste de points objets.
            imgpoints (list): Liste de points d'image.
            rvecs (list): Vecteurs de rotation estimés par la calibration.
            tvecs (list): Vecteurs de translation estimés par la calibration.
            mtx (numpy.array): Matrice de calibration de la caméra.
            dist (numpy.array): Coefficients de distortion.
            image_shape (tuple): Dimensions de l'image (hauteur, largeur).

        Returns:
            tuple: Erreur de reprojection moyenne (float) et une image (numpy.array) 
                   visualisant l'erreur de reprojection.
        """
        total_error = 0
        error_image = np.zeros((image_shape[0], image_shape[1], 3), dtype=np.uint8)

        for i in range(len(objpoints)):
            imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
            error = cv2.norm(imgpoints[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
            total_error += error

            for j in range(len(imgpoints[i])):
                point_error = np.linalg.norm(imgpoints[i][j] - imgpoints2[j][0])

                green_value = 255 - min(255, int(point_error * 25))
                red_value = min(255, int(point_error * 25))
                color = (0, green_value, red_value) if point_error < 10 else (0, red_value, green_value)

                #cv2.circle(error_image, tuple(int(x) for x in imgpoints2[j][0]), 3, color, -1)
                x, y = int(imgpoints2[j][0][0]), int(imgpoints2[j][0][1])
                error_image[y, x] = color 

        average_error = total_error / len(objpoints)

        return average_error, error_image
    
    

    def save_data(self, calib_folder, mtx, dist, erreur_projection):
        """
        Enregistre les données de calibration dans un fichier texte.

        Args:
            calib_folder (str): Chemin du dossier de calibration.
            mtx (numpy.array): Matrice de calibration de la caméra.
            dist (numpy.array): Coefficients de distortion.
            erreur_projection (float): Erreur de reprojection.
        """
        fichier_txt = "data_all_dataset.txt"

        mtx_list = mtx.tolist() if isinstance(mtx, np.ndarray) else mtx
        dist_list = dist.tolist() if isinstance(dist, np.ndarray) else dist

        donnees = f"calib_folder: {calib_folder}\nmtx: {mtx_list}\ndist: {dist_list}\nerreur_projection: {erreur_projection}\n\n"

        # Écriture dans le fichier texte
        with open(fichier_txt, 'a') as fichier:
            fichier.write(donnees)

