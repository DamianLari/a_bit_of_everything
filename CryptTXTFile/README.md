### README.md

# Outil de Chiffrement et Déchiffrement de Fichiers

Ce script Python permet de chiffrer et déchiffrer des fichiers en utilisant la bibliothèque `cryptography`. Il offre une interface en ligne de commande simple pour sélectionner le mode (chiffrement ou déchiffrement) et spécifier le fichier à traiter.

## Fonctionnalités

- **Chiffrement de Fichiers** : Chiffre un fichier avec une clé symétrique générée et stocke le fichier chiffré avec l'extension `.encrypted`.
- **Déchiffrement de Fichiers** : Déchiffre un fichier précédemment chiffré en utilisant la même clé et affiche le contenu du fichier déchiffré.
- **Gestion de la Clé** : Génère et stocke une clé symétrique pour le chiffrement/déchiffrement. Vous pouvez spécifier un fichier clé personnalisé.

## Prérequis

- La bibliothèque `cryptography` doit être installée. Vous pouvez l'installer en utilisant pip :
  ```bash
  pip install cryptography
  ```

## Utilisation

### Commande de Base

Le script se compose de plusieurs options pour chiffrer ou déchiffrer un fichier.

```bash
python main.py <mode> <file_name> [--key_file <key_file>]
```

- `<mode>` : Sélectionnez `encrypt` pour chiffrer un fichier ou `decrypt` pour déchiffrer un fichier.
- `<file_name>` : Nom du fichier à chiffrer ou déchiffrer.
- `--key_file` : (Optionnel) Nom du fichier contenant la clé. Par défaut, "secret.key" est utilisé.

### Exemples

#### Chiffrer un Fichier

Pour chiffrer un fichier `example.txt` avec la clé par défaut :

```bash
python main.py encrypt example.txt
```

Cela générera un fichier chiffré nommé `example.txt.encrypted`.

#### Déchiffrer un Fichier

Pour déchiffrer un fichier `example.txt.encrypted` et afficher son contenu :

```bash
python main.py decrypt example.txt.encrypted
```

Cela générera un fichier déchiffré nommé `example.txt` et affichera son contenu dans le terminal.

#### Utiliser un Fichier de Clé Personnalisé

Si vous souhaitez utiliser un fichier de clé personnalisé, spécifiez le chemin avec l'option `--key_file` :

```bash
python main.py encrypt example.txt --key_file custom_key.key
python main.py decrypt example.txt.encrypted --key_file custom_key.key
```

## Gestion des Erreurs

- Si le fichier clé n'est pas trouvé lors du déchiffrement, le script affichera un message d'erreur et se terminera.
- Si le fichier déchiffré n'est pas un fichier texte lisible, une erreur sera affichée lors de la tentative d'affichage de son contenu.

## Notes

- **Sécurité** : Assurez-vous de protéger le fichier de clé (`secret.key` ou personnalisé) car il est essentiel pour déchiffrer vos fichiers.
- **Compatibilité** : Ce script est conçu pour fonctionner avec des fichiers texte. Les fichiers binaires seront chiffrés/déchiffrés, mais leur contenu ne sera pas affiché correctement dans la console.
