import numpy as np
import cv2
import glob


cameraMatrix1 = np.array([...])
distCoeffs1 = np.array([...])
cameraMatrix2 = np.array([...])
distCoeffs2 = np.array([...])

square_size = 1.0
pattern_size = (8, 6) 
pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
pattern_points *= square_size


obj_points = [] 
img_points1 = [] 
img_points2 = []  


images1 = glob.glob('chemin/vers/images/camera1/*.png')
images2 = glob.glob('chemin/vers/images/camera2/*.png')

for img1, img2 in zip(images1, images2):
    img1 = cv2.imread(img1, 0)
    img2 = cv2.imread(img2, 0)
    
    ret1, corners1 = cv2.findChessboardCorners(img1, pattern_size)
    ret2, corners2 = cv2.findChessboardCorners(img2, pattern_size)
    
    if ret1 and ret2:
        obj_points.append(pattern_points)
        img_points1.append(corners1)
        img_points2.append(corners2)

retval, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, R, T, E, F = cv2.stereoCalibrate(
    obj_points, img_points1, img_points2, cameraMatrix1, distCoeffs1, cameraMatrix2, distCoeffs2, img1.shape[::-1])

print("Matrice de rotation:", R)
print("Vecteur de translation:", T)