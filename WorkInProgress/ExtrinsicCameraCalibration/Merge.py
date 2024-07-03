#!/usr/bin/env python3
import cv2
from cv2 import aruco
import csv
import os
from colorama import Fore, Back, Style
from MocapLoader import MocapLoader
from tag_detection_provider import TagPoseProvider, CameraConfig, TagConfig
from Open3dToolBox import Open3dToolBox
import open3d as o3d
import numpy as np
from scipy.spatial.transform import Rotation as R
import json




class MergeTagPose:
    def __init__(self,tag_config,camera_config, input_mocap_file, output_mocap_file):
        self.tag_detection_provider = TagPoseProvider()
        self.load_global_config(tag_config,camera_config)
        ML = MocapLoader(self.get_grandparent_file_path(input_mocap_file,'datasets/mocap'), self.get_grandparent_file_path(output_mocap_file,'datasets/mocap'))
        self.mocap_data_robot,self.excluded_pose_id = ML.get_mocap_data()
    
    
    def get_grandparent_file_path(self, file_name, subfolder=''):
        #================================
        # Retourne le chemin absolu du fichier spécifié, en partant du répertoire parent du répertoire parent du répertoire courant.
        # Args:
        #   file_name: Nom du fichier.
        #   subfolder: Nom du sous-dossier. Par défaut, il est vide.
        # Returns:
        #   Chemin absolu du fichier.
        #================================
        current_script_path = os.path.realpath(__file__)
        parent_directory_path = os.path.dirname(current_script_path)
        grandparent_directory_path = os.path.dirname(parent_directory_path)

        if subfolder:
            grandparent_directory_path = os.path.join(grandparent_directory_path, subfolder)

        return os.path.join(grandparent_directory_path, file_name)
    
    
    def load_global_config(self,tag_list,camera_list):
        self.tag_config = [TagConfig(tag['type'],tag['size'],tag['dict']) for tag in tag_list]
        self.camera_config = [CameraConfig(camera['name'],camera['images_folder'],*self.load_calib_data(self.tag_detection_provider.get_grandparent_file_path(camera['calibration_file'],'calib'))) for camera in camera_list]
      
       
    def load_calib_data(self,calibration_file):
        #================================
        # Charge les données de calibration depuis le fichier spécifié.
        # Args:
        #   calibration_file: Chemin vers le fichier de calibration.
        # Returns:
        #   matr: Matrice de calibration.
        #   disto: Coefficients de distorsion.
        #================================
        """
        dist = np.array(camera_infos_msg.D)
        mtx = np.array([camera_infos_msg.K[0:3], camera_infos_msg.K[3:6], camera_infos_msg.K[6:9]])
        """
        try:
            with open(calibration_file) as f:
                data = json.load(f)
            matr = data["mtx"]
            disto = data["dist"]
          
        except Exception as e:
            print("Erreur lors de la lecture du fichier de calibration :", e)
        return np.array(matr) , np.array(disto)
    
    def merge_all_pose(self):
        window_positions = [(700, 0), (0, 0)]
        self.multi_pose = []
        for image_id, data in self.mocap_data_robot.items():
            image_file_name = f'image_{image_id}.jpg'  # Nom de l'image basé sur l'ID
            self.multi_pose.append(MultiPose())
            self.multi_pose[image_id].set_id_image(image_id)
            self.multi_pose[image_id].set_robot_pose_from_groundtruth(data)
            for camera in self.camera_config:
                if camera.name != 'niryo':
                    pass
                else:
                    image_path = self.get_grandparent_file_path(image_file_name, camera.image_folder)
                    self.tag_detection_provider.set_calibration_params(*camera.get_calibration_params())
                    if os.path.isfile(image_path):  # Vérifie si l'image existe
                        image = cv2.imread(image_path)
                        cv_image = self.tag_detection_provider.correct_image(image)
                        corners, ids , rvecs, tvecs = self.tag_detection_provider.detect_marker(image,*self.tag_config[0].get_tag_params())
                        
                        #print(self.tag_detection_provider.calculate_positions(ids, rvecs, tvecs))
                        #ids, rota , transla = self.tag_detection_provider.calculate_positions(ids, rvecs, tvecs)
                        ids, rota , transla = self.tag_detection_provider.calculate_positions_in_world_frame(ids, rvecs, tvecs)
                        
                        """
                        [-0.00110253 -0.04765696  0.3614216 ]repère opencv (y en haut, x à droite et z devant) (camera par rapport au tag)
                        
                        
                        """
                        
                        if ids:
                            print(image_id)
                            #rotat = R.from_quat(rvecs[0][0]).as_matrix()
                            #rot = R.from_rotvec([rvecs[0][0], rvecs[0][0][1], rvecs[0][0][2]]).as_quat()
                            self.multi_pose[image_id].set_tag_pose_from_camera(rota[0],transla[0])
                            #cv2.drawFrameAxes(image,*camera.get_calibration_params(),rvecs, tvecs, 0.1)
                            #cv2.imshow(f'Image avec pose du robot {camera.name}', image)
                            """
                            if ids[0] != 210:
                                
                                if camera.name == 'floor':
                                    self.multi_pose[image_id].set_tag_pose_from_camera_floor(rota,transla)
                                    #print(Fore.GREEN,self.tag_detection_provider.calculate_positions(ids, rvecs, tvecs),Style.RESET_ALL)
                                    cv2.namedWindow(f'Image avec pose du robot {camera.name}', cv2.WINDOW_NORMAL)
                                    cv2.moveWindow(f'Image avec pose du robot {camera.name}', *window_positions[0])
                                else:
                                    self.multi_pose[image_id].set_tag_pose_from_camera_top(rota,transla)
                                    #print(Fore.BLUE,self.tag_detection_provider.calculate_positions(ids, rvecs, tvecs),Style.RESET_ALL)
                                    cv2.namedWindow(f'Image avec pose du robot {camera.name}', cv2.WINDOW_NORMAL)
                                    cv2.moveWindow(f'Image avec pose du robot {camera.name}', *window_positions[1])
                            
                                cv2.drawFrameAxes(image,*camera.get_calibration_params(),rvecs[0], tvecs[0], 0.1)
                                
                            else:
                                self.set_rota_transla_none(image_id,camera.name)
                                """
                        else:
                            self.set_rota_transla_none(image_id,camera.name)
                        
                    else:
                        print(f"L'image {image_file_name} n'a pas été trouvée.")
                
            cv2.waitKey(1)
            cv2.destroyAllWindows()
            
    
    def set_rota_transla_none(self,image_id,camera):
        rota = [0,0,0,0]
        transla = [0,0,0]
        if camera == 'niryo':
            self.multi_pose[image_id].set_tag_pose_from_camera(rota,transla)
        else:
            self.multi_pose[image_id].set_tag_pose_from_camera_top(rota,transla)  
                    
        
    
    
    def get_nb_pose(self):
        return len(self.multi_pose)
    
    def get_tag_pose_from_groundtruth(self,image_id):
        #print('self.multi_pose',self.multi_pose[0].get_tag_pose_from_groundtruth())
        return self.multi_pose[image_id].get_tag_pose_from_groundtruth()
    
    def get_tag_pose_from_camera_floor(self,image_id):
        return self.multi_pose[image_id].get_tag_pose_from_camera_floor()
    
    def get_tag_pose_from_camera_top(self,image_id):
        return self.multi_pose[image_id].get_tag_pose_from_camera_top()
    
    def get_robot_pose_from_groundtruth(self,image_id):
        return self.multi_pose[image_id].get_robot_pose_from_groundtruth()
    
    def get_tag_pose_from_camera(self,image_id):
        return self.multi_pose[image_id].get_tag_pose_from_camera()
    
class MultiPose:
    def set_id_image(self,id_image):
        self.id_image = id_image
        
    def set_tag_pose_from_groundtruth(self,pose):
        self.position_from_groundtruth_x = pose['X']
        self.position_from_groundtruth_y = pose['Y']
        self.position_from_groundtruth_z = pose['Z']
        self.orientation_from_groundtruth_x = pose['rotX']
        self.orientation_from_groundtruth_y = pose['rotY']
        self.orientation_from_groundtruth_z = pose['rotZ']
        self.orientation_from_groundtruth_w = pose['rotW']
    
        self.pose_from_groundtruth = pose
    
    def get_tag_pose_from_groundtruth(self):
        return self.pose_from_groundtruth
    
    def set_tag_pose_from_camera(self,rota,transla):
        print(transla)
        print(rota)
        self.position_from_camera_x = transla[0]
        self.position_from_camera_y = transla[1]
        self.position_from_camera_z = transla[2]
        self.orientation_from_camera_x = rota[0]
        self.orientation_from_camera_y = rota[1]
        self.orientation_from_camera_z = rota[2]
        self.pose_from_camera = [transla[0],transla[1],transla[2],rota[0],rota[1],rota[2]]

    def get_tag_pose_from_camera(self):
        return self.pose_from_camera

    def set_tag_pose_from_camera_floor(self,rota,transla):
        
        self.position_from_camera_floor_x = transla[0][0]
        self.position_from_camera_floor_y = transla[0][1]
        self.position_from_camera_floor_z = transla[0][2]
        try:
            self.orientation_from_camera_floor_x = rota[0][0]
            self.orientation_from_camera_floor_y = rota[0][1]
            self.orientation_from_camera_floor_z = rota[0][2]
            self.orientation_from_camera_floor_w = rota[0][3]
            self.pose_from_camera_floor = [transla[0][0],transla[0][1],transla[0][2],rota[0][0],rota[0][1],rota[0][2],rota[0][3]]
        except:
            self.orientation_from_camera_floor_x = rota[0][0]
            self.orientation_from_camera_floor_y = rota[0][1]
            self.orientation_from_camera_floor_z = rota[0][2]
            self.orientation_from_camera_floor_w = rota[0][2]
            self.pose_from_camera_floor = [transla[0][0],transla[0][1],transla[0][2],rota[0][0],rota[0][1],rota[0][2],rota[0][2]]

        
    def get_tag_pose_from_camera_floor(self):
        return self.pose_from_camera_floor
       
    
    def set_tag_pose_from_camera_top(self,rota,transla):
        self.position_from_camera_top_x = transla[0][0]
        self.position_from_camera_top_y = transla[0][1]
        self.position_from_camera_top_z = transla[0][2]
        self.orientation_from_camera_top_x = rota[0][0]
        self.orientation_from_camera_top_y = rota[0][1]
        self.orientation_from_camera_top_z = rota[0][2]
        self.orientation_from_camera_top_w = rota[0][3]
        self.pose_from_camera_top = [transla[0][0],transla[0][1],transla[0][2],rota[0][0],rota[0][1],rota[0][2],rota[0][3]]
        
    def get_tag_pose_from_camera_top(self):
        return self.pose_from_camera_top
    
    def set_robot_pose_from_groundtruth(self,pose):
        try:
            self.position_robot_from_groundtruth_x = pose['X']
            self.position_robot_from_groundtruth_y = pose['Y']
            self.position_robot_from_groundtruth_z = pose['Z']
            self.orientation_robot_from_groundtruth_x = pose['rotX']
            self.orientation_robot_from_groundtruth_y = pose['rotY']
            self.orientation_robot_from_groundtruth_z = pose['rotZ']
            self.orientation_robot_from_groundtruth_w = pose['rotW']
        except:
            self.position_robot_from_groundtruth_x = pose['x']
            self.position_robot_from_groundtruth_y = pose['y']
            self.position_robot_from_groundtruth_z = pose['z']
            self.orientation_robot_from_groundtruth_x = pose['roll']
            self.orientation_robot_from_groundtruth_y = pose['pitch']
            self.orientation_robot_from_groundtruth_z = pose['yaw']
        
        self.pose_robot_from_groundtruth = pose
    
    def get_robot_pose_from_groundtruth(self):
        return self.pose_robot_from_groundtruth
        

if __name__ == '__main__':
    
    input_file_path = "pose_list1.csv"
    output_file_path = "pose_new_format.csv"
        
    tag_list = []
    camera_list = []

    tag_config = {'type': 'apriltag', 'size': 0.123, 'dict': 'tag36h11'}
    tag_list.append(tag_config)

    camera_config = {'name':'floor','calibration_file': 'calib_floor.json', 'images_folder': 'datasets/floor_image'}
    #camera_list.append(camera_config)
    camera_config = {'name':'top','calibration_file': 'calib_top.json', 'images_folder': 'datasets/top_image'}
    #camera_list.append(camera_config)
    camera_config = {'name':'niryo','calibration_file': 'calib_niryo.json', 'images_folder': 'datasets/image_niryo1'}
    camera_list.append(camera_config)


    all_poses = MergeTagPose(tag_list, camera_list,input_file_path,output_file_path)
    all_poses.merge_all_pose()
    


