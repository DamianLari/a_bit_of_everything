# Convertisseur d'Unités

Ce script Python permet de convertir entre différentes unités de distance, poids, volume et température. Il est facile à utiliser via la ligne de commande, et prend en charge un large éventail d'unités couramment utilisées.

## Fonctionnalités

- **Conversions de Distance** : Convertir entre mètres, kilomètres, centimètres, millimètres, miles, yards, pieds, et pouces.
- **Conversions de Poids** : Convertir entre grammes, kilogrammes, milligrammes, livres, onces, et stones.
- **Conversions de Volume** : Convertir entre litres, millilitres, mètres cubes, centimètres cubes, pouces cubes, pieds cubes, gallons, quarts, et pintes.
- **Conversions de Température** : Convertir entre Celsius, Fahrenheit, et Kelvin.

## Utilisation

### Exécution du Script

Utilisez la ligne de commande pour exécuter le script en spécifiant le type de conversion, la valeur à convertir, l'unité de départ, et l'unité d'arrivée. 

#### Syntaxe

```bash
python main.py <type> <valeur> <unité_de_départ> <unité_d_arrivée>
```

#### Exemples

1. **Conversion de Distance** :
    ```bash
    python main.py distance 100 m km
    ```

2. **Conversion de Poids** :
    ```bash
    python main.py weight 150 lb kg
    ```

3. **Conversion de Volume** :
    ```bash
    python main.py volume 1 gal l
    ```

4. **Conversion de Température** :
    ```bash
    python main.py temperature 25 C F
    ```

Voici les tableaux divisés en quatre catégories selon le type de données :

### Tableau des Unités de Distance

| Nom Complet           | Abréviation |
|-----------------------|-------------|
| Mètre                 | m           |
| Kilomètre             | km          |
| Centimètre            | cm          |
| Millimètre            | mm          |
| Mile                  | mi          |
| Yard                  | yd          |
| Pied                  | ft          |
| Pouce                 | in          |

### Tableau des Unités de Poids

| Nom Complet           | Abréviation |
|-----------------------|-------------|
| Gramme                | g           |
| Kilogramme            | kg          |
| Milligramme           | mg          |
| Livre                 | lb          |
| Once                  | oz          |
| Stone                 | stone       |

### Tableau des Unités de Volume

| Nom Complet           | Abréviation |
|-----------------------|-------------|
| Litre                 | l           |
| Millilitre            | ml          |
| Mètre cube            | m3          |
| Centimètre cube       | cm3         |
| Pouce cube            | in3         |
| Pied cube             | ft3         |
| Gallon                | gal         |
| Quart                 | qt          |
| Pinte                 | pt          |


### Tableau des Unités de Température

| Nom Complet           | Abréviation |
|-----------------------|-------------|
| Celsius               | C           |
| Fahrenheit            | F           |
| Kelvin                | K           |