import speech_recognition as sr

def audio_to_text(audio_file, output_text_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
    
    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(text)

audio_file = "chemin/vers/votre_audio.wav"
output_text_file = "chemin/vers/votre_fichier.txt"
audio_to_text(audio_file, output_text_file)