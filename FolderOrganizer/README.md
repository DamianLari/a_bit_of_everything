# Script d'Organisation de Dossiers

Ce script Python organise automatiquement les fichiers dans un ou plusieurs dossiers spécifiés en les classant dans des sous-dossiers basés sur leur extension de fichier. Cela peut aider à maintenir un espace de travail numérique propre et bien organisé.

## Fonctionnalités

- **Organisation Automatique** : Trie les fichiers dans des sous-dossiers basés sur leurs extensions.
- **Supporte Plusieurs Dossiers** : Capable de traiter plusieurs dossiers en une seule exécution.

## Prérequis

Pour exécuter ce script, vous aurez besoin de Python installé sur votre système. Vous pouvez télécharger Python et obtenir des instructions d'installation sur [python.org](https://www.python.org/downloads/).

## Installation

Aucune installation supplémentaire n'est nécessaire en dehors de Python. Assurez-vous simplement que Python est correctement installé sur votre machine.

## Utilisation
**Exécutez le script** en utilisant la commande suivante :
   ```bash
   python main.py chemin_du_dossier1 chemin_du_dossier2 ...
   ```
   Remplacez `nom_dossier1 nom_dossier2 ...` par les chemins des dossiers que vous souhaitez organiser.

### Arguments du Script

- `directories` : Spécifiez les répertoires que vous souhaitez organiser. Vous pouvez passer un ou plusieurs répertoires comme arguments.

## Exemple de Commande

Pour organiser les fichiers dans les dossiers `Documents` et `Downloads`, utilisez :
```bash
python main.py C:/Users/VotreNom/Documents C:/Users/VotreNom/Downloads
```