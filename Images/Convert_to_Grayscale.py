from PIL import Image

def convert_to_grayscale(image_file, output_file):
    with Image.open(image_file) as img:
        grayscale = img.convert("L")
        grayscale.save(output_file)

# Exemple d'utilisation
image_file = "chemin/vers/votre_image.png"
output_file = "chemin/vers/votre_image_grayscale.png"
convert_to_grayscale(image_file, output_file)