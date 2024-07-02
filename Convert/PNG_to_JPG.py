from PIL import Image

def png_to_jpg(png_file, jpg_file):
    # Ouvre le fichier PNG
    with Image.open(png_file) as img:
        # Convertit l'image en mode RGB
        rgb_img = img.convert('RGB')
        # Sauvegarde l'image en format JPG
        rgb_img.save(jpg_file, format='JPEG')

# Exemple d'utilisation
png_file = "Input/InputFile.png"
jpg_file = "Output/OutputFile.jpg"
png_to_jpg(png_file, jpg_file)
