import paho.mqtt.client as mqtt
import time
from pyniryo import *

# Initialisation du NiryoRobot avec son adresse IP
robot = NiryoRobot("192.168.0.103")

# Calibration automatique du robot et mise à jour de son outil
robot.calibrate_auto() #Calibration automatique du robot
robot.update_tool() #Mise à jour de l'outil (detection de l'outil connecté)

# Création d'une instance de client MQTT
client = mqtt.Client()

# Dictionnaire pour stocker les retours des messages MQTT
feedbacks = {}

def on_message(client, userdata, message):
    """
    Fonction de rappel appelée lors de la réception d'un message.
    Elle décode le message et stocke le statut dans le dictionnaire feedbacks.

    Args:
    client: Instance du client MQTT.
    userdata: Données utilisateur privées définies dans Client() ou userdata_set().
    message: Instance de MQTTMessage avec les membres topic, payload, qos, retain.
    """
    msg = str(message.payload.decode("utf-8"))
    print("message received ", msg)
    process, status = msg.split(" ")
    feedbacks[process] = status

def on_connect(client, userdata, flags, rc):
    """
    Fonction de rappel appelée lors de la connexion du client au broker MQTT.
    Elle souscrit au topic 'robot1'.

    Args:
    client: Instance du client MQTT.
    userdata: Données utilisateur privées définies dans Client() ou userdata_set().
    flags: Flags de réponse envoyés par le broker.
    rc: Résultat de la connexion.
    """
    print("Connected with result code " + str(rc))
    client.subscribe("robot1")

client.on_connect = on_connect
client.on_message = on_message

def getStatus(etapeName):
    """
    Fonction pour obtenir le statut d'un processus spécifique à partir du dictionnaire feedbacks.

    Args:
    etapeName: Nom du processus pour lequel obtenir le statut.

    Returns:
    Statut du processus ou None si le processus n'est pas trouvé.
    """
    time.sleep(0.05)
    return feedbacks.get(etapeName)

def waitForStatus(etapeName, status):
    """
    Fonction pour attendre un statut spécifique d'un processus. Elle vérifie continuellement le statut
    et ne poursuit que lorsque le statut désiré est atteint.

    Args:
    etapeName: Nom du processus pour lequel vérifier le statut.
    status: Le statut à attendre.
    """
    while getStatus(etapeName) != status:
        print(f"{etapeName} en cours")
        time.sleep(0.05)
    print(f"{etapeName} {status}")

client.connect("127.0.0.1", 1883, 60)
client.loop_start()

# etape 1
try:
    robot.release_with_tool()
    robot.move_pose(0.2, -0.2, 0.2, 0, 1.57, 0)
    client.publish("robot1", "process1 OK")
except Exception as e:
    print(f"Error: {e}")
    client.publish("robot1", "process1 KO")

# Attente de la fin de l'étape 1
waitForStatus("process1", "OK")

# etape 2 : Déplacement à une autre pose et saisie avec l'outil
try:
    robot.move_pose(0.2, -0.2, 0.2, 0, 1.57, 0)
    robot.grasp_with_tool()
    client.publish("robot1", "process2 OK")
except Exception as e:
    print(f"Error: {e}")
    client.publish("robot1", "process2 KO")

# Attente de la fin de l'étape 2
waitForStatus("process2", "OK")

# etape 3 : Déplacement vers une autre pose
try:
    robot.move_pose(0.2, 0.2, 0.2, 0, 1.57, 0)
    client.publish("robot1", "process3 OK")
except Exception as e:
    print(f"Error: {e}")
    client.publish("robot1", "process3 KO")

# Attente de la fin de l'étape 3
waitForStatus("process3", "OK")

# etape 4 : Déplacement vers la pose finale et libération de l'outil
try:
    robot.move_pose(0.2, 0.2, 0.2, 0, 1.57, 0)
    robot.release_with_tool()
    client.publish("robot1", "process4 OK")
except Exception as e:
    print(f"Error: {e}")
    client.publish("robot1", "process4 KO")

client.loop_stop()
client.disconnect()
