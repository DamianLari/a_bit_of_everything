import numpy as np
import cv2
import json
from pyniryo import NiryoRobot
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

class TransformationHandler:
    def __init__(self, calibration_file):
        self.load_calibration_results(calibration_file)

    def load_calibration_results(self, calibration_file):
        with open(calibration_file) as f:
            data = json.load(f)
        self.R_cam_to_gripper = np.array(data["R_cam_to_gripper"])
        self.t_cam_to_gripper = np.array(data["t_cam_to_gripper"]).reshape(3, 1)

    def create_homogeneous_transform(self, R, t):
        H = np.eye(4)
        H[0:3, 0:3] = R
        H[0:3, 3] = t.flatten()
        return H

    def calculate_transformations(self, gripper_pose, tag_translation, tag_rotation):
        gripper_to_base_translation = np.array(gripper_pose[:3])
        gripper_to_base_rotation = R.from_euler('ZYX', np.flip(gripper_pose[3:]), degrees=False)

        tag_to_camera_translation = np.array(tag_translation)
        tag_to_camera_rotation = R.from_euler('ZYX', tag_rotation, degrees=False)

        T_cam_to_gripper = self.create_homogeneous_transform(self.R_cam_to_gripper, self.t_cam_to_gripper)
        T_gripper_to_base = self.create_homogeneous_transform(gripper_to_base_rotation.as_matrix(), gripper_to_base_translation)
        T_tag_to_camera = self.create_homogeneous_transform(tag_to_camera_rotation.as_matrix(), tag_to_camera_translation)

        T_base_to_camera = T_gripper_to_base @ T_cam_to_gripper
        T_base_to_tag = T_base_to_camera @ T_tag_to_camera

        return T_base_to_camera, T_base_to_tag

class LiveVisualizer:
    def __init__(self, robot_ip, calibration_file):
        self.robot = NiryoRobot(robot_ip)
        self.transformation_handler = TransformationHandler(calibration_file)
        self.all_T_base_to_tag = []
        self.nb_pose = 0

    def start_visualization(self):
        self.robot.set_learning_mode(True)
        while self.nb_pose < 500000:
            np_data = np.frombuffer(self.robot.get_img_compressed(), np.uint8)
            image = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
            gripper_pose = PoseObject.to_list(self.robot.get_pose())

            corners, ids, rvecs, tvecs = self.detect_tags(image)
            if ids is not None:
                self.process_tags(gripper_pose, ids, rvecs, tvecs)

            self.nb_pose += 1
        self.robot.close_connection()
        self.calculate_and_display_average_transform()

    def detect_tags(self, image):
        # Utilisez votre méthode de détection de tags ici
        return corners, ids, rvecs, tvecs

    def process_tags(self, gripper_pose, ids, rvecs, tvecs):
        ids, rota, transla = self.tag_detection_provider.calculate_positions_in_world_frame(ids, rvecs, tvecs)
        T_base_to_camera, T_base_to_tag = self.transformation_handler.calculate_transformations(gripper_pose, transla[0], rota[0])
        self.all_T_base_to_tag.append(T_base_to_tag)

    def calculate_and_display_average_transform(self):
        # Calculez la transformation moyenne ici
        pass

if __name__ == "__main__":
    live_view = LiveVisualizer("192.168.0.103", "hand_eye_calibration_results.json")
    live_view.start_visualization()
