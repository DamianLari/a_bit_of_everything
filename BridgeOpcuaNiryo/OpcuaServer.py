import asyncio
import logging
from asyncua import Server

async def main():
    logging.basicConfig(level=logging.DEBUG)
    _logger = logging.getLogger(__name__)

    # Configuration du serveur
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://127.0.0.1:4840/freeopcua/server/")
    uri = "opcua_mlf"
    idx = await server.register_namespace(uri)

    # Liste de dictionnaires représentant chaque robot et ses processus
    robots_processes = {
        "robot1": ["process1", "process2", "process3", "process4"],
        "robot2": ["process1", "process2", "process3", "process4"],
        # Ajoutez d'autres robots et leurs processus ici
    }

    # Création des variables pour chaque robot et ses processus
    for robot, processes in robots_processes.items():
        robot_obj = await server.nodes.objects.add_object(idx, robot)
        for process in processes:
            tmpVar = await robot_obj.add_variable(idx, process, "Ready")
            await tmpVar.set_writable()
            _logger.info(f"Variable created for {robot}: {process}")

    _logger.info("Server is now starting")
    async with server:
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
