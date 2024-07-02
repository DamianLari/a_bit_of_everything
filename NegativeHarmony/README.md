
# MIDI Inversion et Lecture

Ce projet fournit des fonctions pour inverser les notes d'un fichier MIDI autour d'un point d'inversion et pour lire des fichiers MIDI.

## Table des Matières
1. [Pré-requis](#pré-requis)
2. [Installation](#installation)
3. [Utilisation](#utilisation)
    - [Inverser un fichier MIDI](#inverser-un-fichier-midi)
    - [Lire un fichier MIDI](#lire-un-fichier-midi)
4. [Exemple](#exemple)
5. [Notes](#notes)

## Pré-requis

- Python 3.x
- `pygame` pour la lecture des fichiers MIDI
- `mido` pour la manipulation des fichiers MIDI

## Installation

Installez les dépendances nécessaires en utilisant pip :

```bash
pip install pygame mido
```

## Utilisation

### Inverser un fichier MIDI

La fonction `invert_midi` prend un fichier MIDI en entrée, inverse les notes autour d'un point d'inversion, et sauvegarde le résultat dans un nouveau fichier MIDI.

```python
def invert_midi(input_file, output_file, inversion_point=60):
    original_midi = MidiFile(input_file)
    inverted_midi = MidiFile()

    for track in original_midi.tracks:
        new_track = MidiTrack()
        inverted_midi.tracks.append(new_track)

        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                msg.note = 2 * inversion_point - msg.note
            new_track.append(msg)
    inverted_midi.save(output_file)
```

### Lire un fichier MIDI

La fonction `play_midi` utilise `pygame` pour lire un fichier MIDI.

```python
def play_midi(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)
```


## Notes

- Assurez-vous que les fichiers MIDI spécifiés existent dans le répertoire de travail.
- Le point d'inversion par défaut est défini à 60 (correspondant au C4). Vous pouvez le modifier en passant un autre argument à la fonction `invert_midi`.
- `pygame` peut nécessiter des bibliothèques supplémentaires pour fonctionner correctement sur certaines plateformes. Veuillez consulter la [documentation de pygame](https://www.pygame.org/docs/) pour plus d'informations.
