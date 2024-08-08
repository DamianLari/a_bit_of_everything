# Script de Création de Fichiers et Dossiers Aléatoires

Ce script Python permet de créer automatiquement des fichiers et des sous-dossiers avec un contenu de base dans un ou plusieurs répertoires spécifiés. Il est conçu pour générer rapidement une structure de fichiers à des fins de test ou de développement.

## Fonctionnalités

- Création multiple de fichiers et sous-dossiers dans les répertoires spécifiés.
- Personnalisation du nombre de fichiers et sous-dossiers.
- Choix des extensions de fichiers parmi une liste prédéfinie.

## Utilisation
 **Exécuter le script** :
   Utilisez la commande suivante pour lancer le script :
   ```bash
   python main.py [options] nom_dossier1 nom_dossier2 ...
   ```
   Remplacez `nom_dossier1 nom_dossier2 ...` par les noms des dossiers où vous souhaitez créer des fichiers et des sous-dossiers.

### Arguments du script

- `directory` : Spécifiez un ou plusieurs répertoires de base pour la création de fichiers et sous-dossiers.
- `--num_files` (optionnel) : Nombre de fichiers à créer dans chaque répertoire de base (par défaut : 10).
- `--num_subfolders` (optionnel) : Nombre de sous-dossiers à créer dans chaque répertoire de base (par défaut : 3).
- `--num_files_in_subfolder` (optionnel) : Nombre de fichiers à créer dans chaque sous-dossier (par défaut : 5).
- `--extensions` (optionnel) : Liste des extensions de fichiers à utiliser (ex. `txt png jpeg`). Par défaut : `txt png jpeg js py mp4 csv json html css`

## Exemple de Commande

```bash
python main.py nom_du_dossier nom_dossier2 --num_files 15 --num_subfolders 10 --num_files_in_subfolder 10 --extensions txt png jpeg
```

Cette commande créera 15 fichiers et 10 sous-dossiers dans chacun des répertoires `nom_dossier` et `nom_dossier2`, avec chaque sous-dossier contenant 10 fichiers ayant des extensions spécifiées.
