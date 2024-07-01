import pygame
import time
import mido
from mido import MidiFile, MidiTrack, Message

def play_midi(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)




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

input_file = 'InputFile.mid'
output_file = 'OutputFile.mid'
invert_midi(input_file, output_file)

file_path = 'OutputFile.mid'
play_midi(file_path)
