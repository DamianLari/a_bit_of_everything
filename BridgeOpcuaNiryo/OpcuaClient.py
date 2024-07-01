

import asyncio
from pyniryo import NiryoRobot
from asyncua import Client

# Configuration du robot et du serveur OPC UA
ROBOT_IP = "192.168.0.103"
OPC_UA_SERVER_URL = "opc.tcp://localhost:4840/freeopcua/server/"
NAMESPACE = "opcua_mlf"

async def set_status(client, namespace_index, robot_name, process_name, status):
    """
    Écrit le statut d'un processus dans une variable du serveur OPC UA.

    Args:
    client: Instance du client OPC UA.
    namespace_index: Index de l'espace de noms du serveur OPC UA.
    robot_name: Nom du robot.
    process_name: Nom du processus.
    status: Statut à écrire.
    """
    var = await client.nodes.root.get_child(
        f"0:Objects/{namespace_index}:{robot_name}/{namespace_index}:{process_name}"
    )
    await var.write_value(status)

async def get_status(client, namespace_index, robot_name, process_name):
    """
    Lit le statut d'un processus dans une variable du serveur OPC UA.

    Args:
    client: Instance du client OPC UA.
    namespace_index: Index de l'espace de noms du serveur OPC UA.
    robot_name: Nom du robot.
    process_name: Nom du processus.

    Returns:
    Statut du processus.
    """
    var = await client.nodes.root.get_child(
        f"0:Objects/{namespace_index}:{robot_name}/{namespace_index}:{process_name}"
    )
    return await var.read_value()

async def waitForStatus(client, namespace_index, robot_name, process_name, status):
    while await get_status(client, namespace_index, robot_name, process_name) != status:
        await asyncio.sleep(0.1)

async def robot_task(robot, client, nsidx, robot_name):
    """
    Effectue les tâches du robot et met à jour le statut sur le serveur OPC UA.

    Args:
    robot: Instance du NiryoRobot.
    client: Instance du client OPC UA.
    nsidx: Index de l'espace de noms OPC UA.
    robot_name: Nom du robot.
    """
    try:
        # Étape 1
        robot.release_with_tool()
        robot.move_pose(0.2, -0.2, 0.2, 0, 1.57, 0)
        await set_status(client, nsidx, robot_name, "process1", "OK")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tâches robotiques : {e}")
        # Mettre à jour le statut avec "KO" en cas d'erreur
        await set_status(client, nsidx, robot_name, "process1", "KO")


    try:
        if await get_status(client, nsidx, robot_name, "process1") == "OK":
            robot.move_pose(0.2, -0.2, 0.15, 0, 1.57, 0)
            robot.grasp_with_tool()
            await set_status(client, nsidx, robot_name, "process2", "OK")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tâches robotiques : {e}")
        # Mettre à jour le statut avec "KO" en cas d'erreur
        await set_status(client, nsidx, robot_name, "process2", "KO")


    await waitForStatus(client, nsidx, robot_name, "process2", "OK")
    try:
        robot.move_pose(0.2, 0.2, 0.15, 0, 1.57, 0)
        robot.grasp_with_tool()
        await set_status(client, nsidx, robot_name, "process3", "OK")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tâches robotiques : {e}")
        # Mettre à jour le statut avec "KO" en cas d'erreur
        await set_status(client, nsidx, robot_name, "process3", "KO")


    await waitForStatus(client, nsidx, robot_name, "process3", "OK")
    try:
        robot.move_pose(0.2, 0.2, 0.15, 0, 1.57, 0)
        robot.release_with_tool()
        await set_status(client, nsidx, robot_name, "process4", "OK")
    except Exception as e:
        print(f"Erreur lors de l'exécution des tâches robotiques : {e}")
        # Mettre à jour le statut avec "KO" en cas d'erreur
        await set_status(client, nsidx, robot_name, "process4", "KO")

        
async def main():
    # Initialisation et calibration du robot
    robot = NiryoRobot(ROBOT_IP)
    robot.calibrate_auto()
    robot.update_tool()

    print(f"Connexion au serveur OPC UA à {OPC_UA_SERVER_URL} ...")
    async with Client(url=OPC_UA_SERVER_URL) as client:
        nsidx = await client.get_namespace_index(NAMESPACE)
        print(f"Index de l'espace de noms pour '{NAMESPACE}': {nsidx}")

        # Lancement des tâches robotiques et mise à jour du statut
        await robot_task(robot, client, nsidx, "robot1")

        # Fermeture du robot
        robot.close_connection()

if __name__ == "__main__":
    asyncio.run(main())
