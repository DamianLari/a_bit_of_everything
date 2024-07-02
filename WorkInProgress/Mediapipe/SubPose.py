import json
import pygame
import paho.mqtt.client as mqtt
import mediapipe as mp

mqtt_broker = "127.0.0.1"
mqtt_port = 1883

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Animation Corporelle')
clock = pygame.time.Clock()

hand_landmarks = []
face_landmarks = []
body_landmarks = []

HAND_CONNECTIONS = [
    # Doigts
    (0, 1), (1, 2), (2, 3), (3, 4),  # Pouce
    (0, 5), (5, 6), (6, 7), (7, 8),  # Index
    (5, 9), (9, 10), (10, 11), (11, 12),  # Majeur
    (9, 13), (13, 14), (14, 15), (15, 16),  # Annulaire
    (13, 17), (17, 18), (18, 19), (19, 20)  # Petit doigt
]

FACE_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4), # Exemple
]

BODY_CONNECTIONS = [
    (11, 13), (13, 15),  # Bras gauche
    (12, 14), (14, 16),  # Bras droit
    (11, 23), (23, 25),  # Jambe gauche
    (12, 24), (24, 26),  # Jambe droite
    # à ajouter -> le buste, les épaules, etc.
]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

def process_face_mesh(image_rgb):
    results = face_mesh.process(image_rgb)
    if results.multi_face_landmarks:
        return [landmark for face_landmarks in results.multi_face_landmarks for landmark in face_landmarks.landmark]
    return []

def on_message(client, userdata, message):
    global hand_landmarks, face_landmarks, body_landmarks
    if message.topic == "mediapipe/hands":
        hand_landmarks = json.loads(message.payload.decode("utf-8"))
    elif message.topic == "mediapipe/face":
        face_landmarks = json.loads(message.payload.decode("utf-8"))
    elif message.topic == "mediapipe/pose":
        body_landmarks = json.loads(message.payload.decode("utf-8"))

mqtt_client = mqtt.Client("mediapipe_subscriber")
mqtt_client.connect(mqtt_broker, mqtt_port, 60)
mqtt_client.subscribe([("mediapipe/hands", 0), ("mediapipe/face", 0),("mediapipe/pose", 0)])
mqtt_client.on_message = on_message
mqtt_client.loop_start()

def draw_connections(landmarks, connections, color=(255, 255, 255)):
    for connection in connections:
        start_idx, end_idx = connection
        if start_idx < len(landmarks) and end_idx < len(landmarks):
            start_lm = landmarks[start_idx]
            end_lm = landmarks[end_idx]
            start_x, start_y = int(start_lm['x'] * 800), int(start_lm['y'] * 600)
            end_x, end_y = int(end_lm['x'] * 800), int(end_lm['y'] * 600)
            pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_connections(hand_landmarks, HAND_CONNECTIONS)
    draw_connections(face_landmarks, FACE_CONNECTIONS, color=(0, 255, 255))
    draw_connections(body_landmarks, BODY_CONNECTIONS, color=(255, 0, 0))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
mqtt_client.loop_stop()
mqtt_client.disconnect()
