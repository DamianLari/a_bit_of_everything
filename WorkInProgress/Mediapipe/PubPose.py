import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt
import json

mqtt_client = mqtt.Client("mediapipe_publisher")
mqtt_broker = "127.0.0.1"  
mqtt_port = 1883

mqtt_client.connect(mqtt_broker, mqtt_port, 60)

mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_face_detection.FaceDetection()
hands = mp_hands.Hands()
pose = mp_pose.Pose()

def publish_landmarks(topic, data):
    if topic == "mediapipe/face":
        landmarks_data = [{
            "id": idx,
            "bounding_box": {
                "x_min": detection.location_data.relative_bounding_box.xmin,
                "y_min": detection.location_data.relative_bounding_box.ymin,
                "width": detection.location_data.relative_bounding_box.width,
                "height": detection.location_data.relative_bounding_box.height
            }
        } for idx, detection in enumerate(data)]
    else:
        landmarks_data = [{"id": idx, "x": lm.x, "y": lm.y} for idx, lm in enumerate(data)]

    mqtt_client.publish(topic, json.dumps(landmarks_data))

def process_face(image_rgb):
    results = face_detection.process(image_rgb)
    return results.detections if results.detections else []

def process_hands(image_rgb):
    results = hands.process(image_rgb)
    return results.multi_hand_landmarks if results.multi_hand_landmarks else []

def process_pose(image_rgb):
    results = pose.process(image_rgb)
    return results.pose_landmarks if results.pose_landmarks else []

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Échec de la capture de l'image de la webcam.")
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    face_landmarks = process_face(image_rgb)
    if face_landmarks:
        publish_landmarks("mediapipe/face", face_landmarks)

    hand_landmarks = process_hands(image_rgb)
    if hand_landmarks:
        for hand in hand_landmarks:
            publish_landmarks("mediapipe/hands", hand.landmark)

    pose_landmarks = process_pose(image_rgb)
    if pose_landmarks:
        publish_landmarks("mediapipe/pose", pose_landmarks.landmark)

    cv2.imshow('MediaPipe Detection', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
mqtt_client.disconnect()
