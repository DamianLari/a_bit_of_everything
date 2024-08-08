# Outil de Calcul de Dates

Ce script Python permet d'effectuer des calculs simples sur les dates, tels que calculer la différence en jours entre deux dates, ajouter des jours à une date spécifique, ou encore soustraire des jours d'une date donnée. Le script utilise `argparse` pour permettre l'utilisation de différentes commandes en ligne de commande.

## Fonctionnalités

- **Calculer la différence entre deux dates** : Calcule le nombre de jours entre deux dates spécifiées.
- **Ajouter des jours à une date** : Ajoute un nombre spécifié de jours à une date donnée.
- **Soustraire des jours d'une date** : Soustrait un nombre spécifié de jours d'une date donnée.


## Utilisation

Le script se compose de plusieurs sous-commandes qui effectuent différentes opérations. Vous pouvez utiliser les commandes suivantes pour exécuter les différentes fonctionnalités du script.

### 1. Calculer la différence entre deux dates

Utilisez la sous-commande `diff` pour calculer la différence en jours entre deux dates spécifiées.

```bash
python main.py diff <date1> <date2>
```

#### Exemple :

```bash
python main.py diff 2023-08-01 2024-08-01
```

### 2. Ajouter des jours à une date

Utilisez la sous-commande `add` pour ajouter un nombre de jours spécifié à une date donnée.

```bash
python main.py add <date> <jours>
```

#### Exemple :

```bash
python main.py add 2023-08-01 30
```

### 3. Soustraire des jours d'une date

Utilisez la sous-commande `sub` pour soustraire un nombre de jours spécifié d'une date donnée.

```bash
python main.py sub <date> <jours>
```

#### Exemple :

```bash
python main.py sub 2024-08-01 15
```

## Options

- `<date1>` et `<date2>` : Les dates doivent être fournies dans le format `YYYY-MM-DD`.
- `<jours>` : Nombre de jours à ajouter ou à soustraire.

## Exemple d'Exécution

```bash
python main.py diff 2023-08-01 2024-08-01
# Sortie: Différence en jours : 365

python main.py add 2023-08-01 30
# Sortie: Nouvelle date après ajout de 30 jours : 2023-08-31

python main.py sub 2024-08-01 15
# Sortie: Nouvelle date après soustraction de 15 jours : 2024-07-17
```
