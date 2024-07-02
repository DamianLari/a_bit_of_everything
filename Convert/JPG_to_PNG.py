from PIL import Image

def jpg_to_png(jpg_file, png_file):
    # Ouvre le fichier JPG
    with Image.open(jpg_file) as img:
        # Sauvegarde l'image en format PNG
        img.save(png_file, format='PNG')

# Exemple d'utilisation
jpg_file = "Input/InputFile.jpg"
png_file = "Output/OutputFile.png"
jpg_to_png(jpg_file, png_file)
