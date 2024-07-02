import cv2
import mediapipe as mp

# Initialisation des modules MediaPipe
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection()
hands = mp_hands.Hands()
hands.max_num_hands = 10
pose = mp_pose.Pose()

# Initialisation de la capture vidéo (Webcam)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Échec de la capture de l'image de la webcam.")
        continue

    # Conversion de l'image de BGR à RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Traitement de l'image et détection des visages, des mains et de la pose
    face_results = face_detection.process(image_rgb)
    hand_results = hands.process(image_rgb)
    pose_results = pose.process(image_rgb)

    image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if face_results.detections:
        for detection in face_results.detections:
            mp_drawing.draw_detection(image, detection)

    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    if pose_results.pose_landmarks:
        mp_drawing.draw_landmarks(image, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Affichage de l'image résultante
    cv2.imshow('MediaPipe Detection', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
