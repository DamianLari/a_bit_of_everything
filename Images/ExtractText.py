import pytesseract
from PIL import Image

def ocr_image(image_file, output_text_file):
    text = pytesseract.image_to_string(Image.open(image_file))
    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Exemple d'utilisation
image_file = "chemin/vers/votre_image.png"
output_text_file = "chemin/vers/votre_fichier.txt"
ocr_image(image_file, output_text_file)