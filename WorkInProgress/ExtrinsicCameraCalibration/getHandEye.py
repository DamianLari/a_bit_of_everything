import numpy as np
import cv2
from scipy.spatial.transform import Rotation as R
import csv
import json
from multi_pose import MultiPose, MergeTagPose

class HandToEyeCalib:
    def __init__(self, input_file_path, output_file_path):
        tag_config = {'type': 'apriltag', 'size': 0.103, 'dict': 'tag36h11'}
        camera_config = {'name': 'niryo', 'calibration_file': 'CalibData_new2.json', 'images_folder': 'datasets/image_niryo3'}

        self.all_poses = MergeTagPose([tag_config], [camera_config], input_file_path, output_file_path)
        self.all_poses.merge_all_pose()
        self.nb_pose = self.all_poses.get_nb_pose() - 1

    def extract_rot_matrix(self, pose):
        try:
            return R.from_quat([pose[3], pose[4], pose[5], pose[6]]).as_matrix()
        except:
            try:
                return R.from_euler('ZYX', [pose[5], pose[4], pose[3]], degrees=False).as_matrix()
            except:
                return R.from_quat([pose['rotX'], pose['rotY'], pose['rotZ'], pose['rotW']]).as_matrix()

    def extract_translation(self, pose):
        try:
            return np.array([pose[0], pose[1], pose[2]])
        except:
            return np.array([pose['x'], pose['y'], pose['z']])

    def get_hand_to_eye(self):
        all_R_target_to_cam = []
        all_t_target_to_cam = []
        all_R_gripper_to_base = []
        all_t_gripper_to_base = []

        for image_id in range(self.nb_pose):
            tag_pose_from_camera = self.all_poses.get_tag_pose_from_camera(image_id)
            robot_pose_from_groundtruth = self.all_poses.get_robot_pose_from_groundtruth(image_id)

            if tag_pose_from_camera != [0, 0, 0, 0, 0, 0]:
                R_gripper_to_base = self.extract_rot_matrix(robot_pose_from_groundtruth)
                t_gripper_to_base = self.extract_translation(robot_pose_from_groundtruth).reshape(3, 1)

                R_target_to_cam = self.extract_rot_matrix(tag_pose_from_camera)
                t_target_to_cam = self.extract_translation(tag_pose_from_camera).reshape(3, 1)

                all_R_target_to_cam.append(R_target_to_cam)
                all_t_target_to_cam.append(t_target_to_cam)

                all_R_gripper_to_base.append(R_gripper_to_base)
                all_t_gripper_to_base.append(t_gripper_to_base)

        self.R_cam_to_gripper, self.t_cam_to_gripper = cv2.calibrateHandEye(
            all_R_gripper_to_base, all_t_gripper_to_base, 
            all_R_target_to_cam, all_t_target_to_cam, 
            cv2.CALIB_HAND_EYE_PARK
        )

        self.save_calibration_results()

    def save_calibration_results(self):
        results = {
            "R_cam_to_gripper": self.R_cam_to_gripper.tolist(),
            "t_cam_to_gripper": self.t_cam_to_gripper.tolist()
        }
        with open("hand_eye_calibration_results.json", "w") as f:
            json.dump(results, f)

if __name__ == "__main__":
    calib = HandToEyeCalib("pose_list3.csv", "pose_new_format.csv")
    calib.get_hand_to_eye()
