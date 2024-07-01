from pyniryo import *
import os
import time
import csv
import numpy as np
import math
import matplotlib.pyplot as plt

"""
topics à écouter:
/niryo_robot_hardware_interface/end_effector_interface/save_pos_button_status (surement la pose de la pince)
/niryo_robot_vision/compressed_video_stream (flux vidéo)
/niryo_robot_vision/camera_intrinsics (paramètres de la caméra)
/tf (interessant: hand_link, base_link) (pdf en annexes)
/tf_static 
/niryo_robot/robot_state
rosbag record /niryo_robot/robot_state /niryo_robot_vision/camera_intrinsics /niryo_robot_vision/compressed_video_stream
"""

# Décorateurs
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Temps d'exécution pour {func.__name__}: {end - start} secondes")
        return result
    return wrapper

def log_results(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as log_file:
            log_file.write(f"{func.__name__} appelée avec {args}, {kwargs} - Résultat: {result}\n")
        return result
    return wrapper

def error_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erreur dans {func.__name__}: {e}")
    return wrapper

def meanPose():
    pose_nb=0
    all_x, all_y, all_z = [], [], []
    all_roll, all_pitch, all_yaw = [], [], []

    while pose_nb<100:
        pose = robot.get_pose()
        all_x.append(pose.x)
        all_y.append(pose.y)
        all_z.append(pose.z)
        all_roll.append(pose.roll)
        all_pitch.append(pose.pitch)
        all_yaw.append(pose.yaw)
        time.sleep(0.1)
        pose_nb+=1

    mean_x, mean_y, mean_z = np.mean(all_x), np.mean(all_y), np.mean(all_z)
    mean_roll, mean_pitch, mean_yaw = np.mean(all_roll), np.mean(all_pitch), np.mean(all_yaw)

    std_x, std_y, std_z = np.std(all_x), np.std(all_y), np.std(all_z)
    std_roll, std_pitch, std_yaw = np.std(all_roll), np.std(all_pitch), np.std(all_yaw)

    print(f"Moyenne X: {mean_x}, Écart-type X: {std_x}")
    print(f"Moyenne Y: {mean_y}, Écart-type Y: {std_y}")
    print(f"Moyenne Z: {mean_z}, Écart-type Z: {std_z}")
    print(f"Moyenne Roll: {mean_roll}, Écart-type Roll: {std_roll}")
    print(f"Moyenne Pitch: {mean_pitch}, Écart-type Pitch: {std_pitch}")
    print(f"Moyenne Yaw: {mean_yaw}, Écart-type Yaw: {std_yaw}")
 
def write_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


@timer
@log_results
@error_handler
def GoBack(nb_move,file_name,trial):
    time.sleep(1)
    start_position = PoseObject(x=0.2, y=-0.0, z=0.3, roll=0, pitch=1.57, yaw=0)
    robot.move_pose(start_position)

    initial_position = robot.get_pose()

    joint_values = [1.5, -0.7, 0.5, -0.5, 0.5, -0.5] 
    number_of_round_trips = 5

    for _ in range(nb_move):
        for i in range(6):
            current_joints = robot.get_joints()
            current_joints[i] += joint_values[i]
            robot.move_joints(current_joints)

            current_joints = robot.get_joints()
            current_joints[i] -= joint_values[i]  
            robot.move_joints(current_joints)

    final_position = robot.get_pose()

    error_3d = calculate_3d_error(initial_position, final_position)
    error_angular = calculate_angular_error(initial_position, final_position)
    
    print("Initial Position:", initial_position)
    print("Final Position:", final_position)
    print("3D Error:", error_3d)
    print("Angular Error:", error_angular)

    write_to_file(file_name, f"Trial: {trial}")
    results = f"3D Error (meters): {error_3d}\nAngular Error (radians): {error_angular}\n"
    write_to_file(file_name, results)

    return error_3d, error_angular

@timer
@log_results
@error_handler
def measure_repeatability_by_joint(nb_move, file_name,trial):
    time.sleep(1)
    start_position = PoseObject(x=0.2, y=-0.2, z=0.2, roll=0, pitch=1.57, yaw=0)
    robot.move_pose(start_position)
    
    errors_3D_by_joint = []
    errors_angular_by_joint = []
    final_angle_difference = []
    percentage_errors_by_joint = []
    
    for i in range(6): 
        initial_position = robot.get_pose()
        initial_angles = robot.get_joints()
        joint_values = [0.5, -0.5, 0.5, -0.5, 0.5, -0.5] 
        total_percentage_error = 0

        for _ in range(nb_move):
            current_joints = robot.get_joints()
            current_joints[i] += joint_values[i]  
            robot.move_joints(current_joints)
            
            current_joints = robot.get_joints()
            current_joints[i] -= joint_values[i]  
            robot.move_joints(current_joints)

        final_position = robot.get_pose()
        final_angles = robot.get_joints()

        angular_movement = abs(joint_values[i] * 2)  
        angle_error = abs(final_angles[i] - initial_angles[i])
        final_angle_difference.append(angle_error)
        
        percentage_error = (angle_error / angular_movement) * 100
        total_percentage_error += percentage_error

        average_percentage_error = total_percentage_error / nb_move
        percentage_errors_by_joint.append(average_percentage_error)

        error_3D = calculate_3d_error(initial_position, final_position)
        errors_3D_by_joint.append(error_3D)

        error_angular = calculate_angular_error(initial_position, final_position)
        errors_angular_by_joint.append(error_angular)

    #errors_3D_by_joint.sort(key=lambda x: x[1])
    #errors_angular_by_joint.sort(key=lambda x: x[1])
    write_to_file(file_name, f"Trial: {trial}")
    for joint, error_3D in enumerate(errors_3D_by_joint):
        print(f"Joint {joint + 1}:3D Error (meters)= {error_3D} |Angular Error (radians)= {errors_angular_by_joint[joint]} | Error in angle (radians) = {final_angle_difference[joint]} | Percentage Error = {percentage_errors_by_joint[joint]}%")
        results = f"Joint {joint + 1}:\n3D Error (meters) = {error_3D}\nSolide Angle Error (radians)= {errors_angular_by_joint[joint]}\n Error in angle (radians) = {final_angle_difference[joint]}\nPercentage Error = {percentage_errors_by_joint[joint]}%\n"
        write_to_file(file_name, results)
    return errors_3D_by_joint, errors_angular_by_joint , final_angle_difference, percentage_errors_by_joint

def calculate_3d_error(pos1, pos2):
    return math.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2 + (pos1.z - pos2.z) ** 2)

def calculate_angular_error(pos1, pos2):
    return math.sqrt((pos1.roll - pos2.roll) ** 2 + (pos1.pitch - pos2.pitch) ** 2 + (pos1.yaw - pos2.yaw) ** 2)


def plot_joint_errors_by_trial(joint_3d_errors, joint_angular_errors, file_name):
    num_trials = len(joint_3d_errors)
    num_joints = len(joint_3d_errors[0])
    joints = np.arange(1, num_joints + 1)
    
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    colors = ['green', 'blue', 'orange']  

    for i in range(num_trials):
        color = colors[i % len(colors)]
        trial_label = f'Trial {i+1}'
        axs[0].bar(joints + 0.1 * i, joint_3d_errors[i], width=0.1, color=color, alpha=0.7, label=trial_label)
        axs[1].bar(joints + 0.1 * i, joint_angular_errors[i], width=0.1, color=color, alpha=0.7, label=trial_label)

    axs[0].set_title('Joint 3D Errors')
    axs[0].set_xlabel('Joint Number')
    axs[0].set_ylabel('3D Error (meters)')

    axs[1].set_title('Joint Angular Errors')
    axs[1].set_xlabel('Joint Number')
    axs[1].set_ylabel('Angular Error (radians)')

    axs[0].legend()
    axs[1].legend()

    plt.tight_layout()
    plt.savefig(file_name)
    

def plot_overall_errors(trial_3d_errors, trial_angular_errors,file_name):
    num_trials = len(trial_3d_errors)
    trials = np.arange(1, num_trials + 1)

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    axs[0].bar(trials, trial_3d_errors, color='blue', alpha=0.7)
    axs[0].set_title('Overall 3D Errors by Trial')
    axs[0].set_xlabel('Trial Number')
    axs[0].set_ylabel('3D Error (meters)')

    axs[1].bar(trials, trial_angular_errors, color='red', alpha=0.7)
    axs[1].set_title('Overall Angular Errors by Trial')
    axs[1].set_xlabel('Trial Number')
    axs[1].set_ylabel('Angular Error (radians)')

    plt.tight_layout()
    plt.savefig(file_name)
    

def plot_angular_error_per_joint(angular_errors_by_joint, file_name):
    num_joints = len(angular_errors_by_joint)
    joints = np.arange(1, num_joints + 1)
    
    plt.figure(figsize=(10, 5))
    
    plt.bar(joints, angular_errors_by_joint, color='orange', alpha=0.7)
    plt.title('Erreurs angulaires par joint')
    plt.xlabel('Numéro du joint')
    plt.ylabel('Erreur angulaire (radians)')
    
    plt.xticks(joints)
    plt.tight_layout()
    plt.savefig(file_name)


robots_ips = ["192.168.0.103"] #, "192.168.0.102"
nb_moves_list = [1, 2, 5, 1] 
file_name = "results.txt"
nb_trial = 3
num_robot = 0
for ip in robots_ips:
    num_robot += 1
    robot = NiryoRobot(ip)
    robot.calibrate_auto()
    robot.update_tool()
    write_to_file(file_name, f"Robot {num_robot} , IP: {ip}")

    for nb_move in nb_moves_list:
        write_to_file(file_name, f"Repetabilité des mouvements. 1 aller retour par joints, joint après joints, {nb_move} fois")
        print(f"Repetabilité des mouvements. 1 aller retour par joints, joint après joints, {nb_move} fois")
        overall_3d_errors = [] 
        overall_angular_errors = [] 
        
        for trial in range(nb_trial):
            print(f"Essai {trial}")
            error_3d, error_solid_angle = GoBack(nb_move, file_name,trial+1)
            overall_3d_errors.append(error_3d)
            overall_angular_errors.append(error_solid_angle)
        plot_overall_errors(overall_3d_errors, overall_angular_errors, f"Robot{num_robot}_overall_errors_for_{nb_move}moves.png")
        
        write_to_file(file_name, f"Comparaison repetabilité des joints. {nb_move} aller-retour par joints. joint après joints")
        print(f"Comparaison repetabilité des joints. {nb_move} aller-retour par joints. joint après joints")
        joint_3d_errors = []
        joint_angular_errors = []

        """
        for trial in range(nb_trial) : 
            print(f"Essai {trial}")
            error_3d,error_solid_angle, errors_angular_by_joint, percentage_errors_by_joint = measure_repeatability_by_joint(nb_move, file_name,trial+1)
            joint_3d_errors.append(error_3d)
            joint_angular_errors.append(error_solid_angle)
            write_to_file(file_name, "\n")
        plot_joint_errors_by_trial(joint_3d_errors, joint_angular_errors, f"Robot{num_robot}_joint_errors_for_{nb_move}moves.png")
        plot_angular_error_per_joint(errors_angular_by_joint, "nom_du_fichier_graphique.png")
        """
    robot.close_connection()

