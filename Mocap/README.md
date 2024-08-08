# Mocap Script

Ce script est conçu pour capturer et traiter les données de mouvement (mocap) à partir d'un système de capture de mouvement, tel que OptiTrack. Il utilise le client NatNet pour recevoir les données de corps rigides en temps réel et enregistre ces données dans des fichiers CSV pour une analyse ultérieure.

## Fonctionnalités

- **Capture de données Mocap en temps réel** : Le script se connecte à un serveur de capture de mouvement via NatNet, reçoit les données de position et de rotation des corps rigides spécifiés et les stocke en temps réel.
- **Enregistrement des données** : Les données capturées sont enregistrées dans un fichier CSV horodaté, qui contient les informations de position et de rotation.
- **Interface Multithread** : Le script utilise des threads pour gérer la réception des données de mouvement et le stockage des données en parallèle, ce qui garantit une capture efficace et non bloquante.

## Prérequis

- **NatNet SDK** : Ce script nécessite le SDK NatNet de OptiTrack pour fonctionner.
- **Python 3.x**
- **Bibliothèques Python** :
  - `datetime`
  - `csv`
  - `threading`
  - `time`
  - `sys`

## Configuration

Avant d'exécuter le script, assurez-vous de configurer correctement les adresses IP pour le client et le serveur de capture de mouvement dans le dictionnaire `optionsDict` :

```python
optionsDict = {}
optionsDict["clientAddress"] = "10.191.76.182"  # Adresse IP du client (machine où le script est exécuté)
optionsDict["serverAddress"] = "10.191.76.211"  # Adresse IP du serveur (système de capture de mouvement)
optionsDict["use_multicast"] = False            # Utiliser ou non le multicast
```

## Utilisation

### Exécution de Base

Pour démarrer la capture de mouvement, exécutez simplement le script à partir de votre terminal ou environnement Python :

```bash
python main.py
```

Le script commencera à recevoir les données des corps rigides spécifiés dans `MocapIndex` et les enregistrera dans un fichier CSV nommé selon la date et l'heure actuelles.

### Interruption

Pour arrêter le script, appuyez sur `Ctrl+C` dans le terminal. Cela arrêtera proprement la capture et fermera tous les fichiers ouverts.

## Structure des Données Enregistrées

Les données de mouvement sont enregistrées dans un fichier CSV avec les colonnes suivantes :

- `time` : Horodatage de l'enregistrement.
- `MocapIndex` : Identifiant du corps rigide capturé.
- `mocapX`, `mocapY`, `mocapZ` : Coordonnées de position du corps rigide.
- `rotX`, `rotY`, `rotZ`, `rotW` : Composants de la rotation quaternion du corps rigide.

## Personnalisation

- **Modifier les corps rigides capturés** : Pour changer les corps rigides dont les données sont capturées, modifiez la liste `MocapIndex` dans le script :

  ```python
  MocapIndex = [15,16]  # Remplacez par les IDs des corps rigides souhaités
  ```

- **Options de capture** : D'autres paramètres de capture peuvent être ajustés dans `optionsDict`, comme l'activation du multicast ou le changement des adresses IP.

## Licence

Ce script est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer comme bon vous semble.

---

Ce `README.md` fournit des informations complètes sur l'utilisation et la configuration de votre script de capture de mouvement, avec des instructions spécifiques pour l'exécution et la personnalisation.