import paho.mqtt.client as mqtt  # Import de la bibliothèque MQTT
import time  # Import de la bibliothèque de gestion du temps
from pyniryo import *  # Import de la bibliothèque pour contrôler un robot Niryo
import json  # Import de la bibliothèque pour manipuler des données JSON
import argparse  # Import de la bibliothèque pour analyser les arguments de ligne de commande

#python sub_niryo.py --BROKER_NAME="cesi_master" --BROKER_IP="127.0.0.1" --BROKER_PORT=1883 --QOS=1 --NYRIO_IP=192.168.0.103

# Définition des arguments à passer dans la ligne de commande pour configurer le client MQTT
parser = argparse.ArgumentParser(description='run mqtt client')
parser.add_argument("-bn", "--BROKER_NAME", help="Nom du broker, par défaut \"cesi_master\"", required=False)
parser.add_argument("-bi", "--BROKER_IP", help="Adresse IP du broker, par défaut \"127.0.0.1\"", required=False)
parser.add_argument("-bp", "--BROKER_PORT", type=int, help="Port du broker, par défaut 1883", required=False)
parser.add_argument("-q", "--QOS", type=int, help="Quality of Service, valeurs possibles 0, 1, 2", required=False)
parser.add_argument("-nip", "--NYRIO_IP", type=str, help="Adresse IP du robot Niryo (utiliser Niryo Studio pour l'identifier)", required=True)
#rodo try expet
# Récupération et affichage des arguments
args = parser.parse_args()
print(args)
BROKER_IP = "127.0.0.1"
BROKER_PORT = 1883

if not args.BROKER_NAME:
    print("no broker name. using cesi_master by default")
    BROKER_NAME = "cesi_master"

if not args.BROKER_IP:
    print("no broker ip. using 127.0.0.1 by default")
    BROKER_IP = "127.0.0.1"

if not args.BROKER_PORT:
    print("no broker port. using 1883 by default")
    BROKER_PORT = 1883

if not args.QOS:
    print("no QOS. using 1 by default")
    QOS = 1


NYRIO_IP = args.NYRIO_IP

# Affichage des paramètres de configuration
print("BROKER_NAME:" + str(BROKER_NAME))
print("BROKER_IP:" + str(BROKER_IP))
print("BROKER_PORT:" + str(BROKER_PORT))
print("NYRIO_IP:" + str(NYRIO_IP))

# Sujets MQTT utilisés pour les informations et commandes
MQTT_TOPIC_INFO = "niryo_state"
MQTT_TOPIC_COMMAND = "niryo_todo"

# Initialisation et configuration du robot Niryo
robot = NiryoRobot(NYRIO_IP)
robot.calibrate_auto()
robot.update_tool()

# Fonction pour publier l'état du robot
def publish_state(message):
    client.publish(MQTT_TOPIC_INFO, message)

# Callback appelé lors de la réception d'un message MQTT
def on_message(client, userdata, message):
    message_decode = message.payload.decode("utf-8")
    print(f"Message reçu: {message_decode}")

    # Définition des fonctions correspondant aux différentes commandes
    def release_with_tool():
        publish_state("Niryo::run release_with_tool start")
        robot.release_with_tool()
        publish_state("Niryo::run release_with_tool finish")

    def grasp_with_tool():
        publish_state("Niryo::run grasp_with_tool start")
        robot.grasp_with_tool()
        publish_state("Niryo::run grasp_with_tool finish")

    def move_pose():
        try:
            cmd = json.loads(message_decode.replace("move_pose", "").strip())
            publish_state("Niryo::run move_pose start")
            robot.move_pose(cmd['x'], cmd['y'], cmd['z'], cmd['rx'], cmd['ry'], cmd['rz'])
            
            publish_state("Niryo::run move_pose finish")
        except (json.JSONDecodeError, KeyError):
            publish_state("Niryo::invalid move_pose command format")
    
    # Dictionnaire liant les commandes reçues aux fonctions correspondantes
    actions = {
        "release_with_tool": release_with_tool,
        "grasp_with_tool": grasp_with_tool,
        "move_pose": move_pose
    }

    # Exécution de la commande reçue
    action_key = message_decode.split()[0]  # Extraction de la commande de la chaîne reçue
    action_func = actions.get(action_key, lambda: print("Niryo::unknown command", message_decode))
    action_func()

# Callback appelé lors de la connexion réussie au
def on_connect(client, userdata, flags, rc):
    print("Connecté avec le code résultat " + str(rc))
    client.subscribe(MQTT_TOPIC_COMMAND)  # Abonnement au sujet des commandes

# Création d'une instance client MQTT
client = mqtt.Client()

# Assignation des callbacks pour la connexion et la réception des messages
client.on_connect = on_connect

client.on_message = on_message

# Connexion au broker MQTT
client.connect(BROKER_IP, BROKER_PORT, 60)

# Démarrage de la boucle de traitement des messages MQTT
client.loop_start()

# Boucle pour maintenir le script en cours d'exécution
try:
    while True:
        time.sleep(1)  # Pause pour réduire l'utilisation du processeur
except KeyboardInterrupt:  # Gestion de l'interruption par l'utilisateur
    print("Fermeture du script")

# Arrêt de la boucle de traitement et déconnexion du client MQTT
client.loop_stop()
client.disconnect()
