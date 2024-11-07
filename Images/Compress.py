from PIL import Image

def compress_image(image_file, output_file, quality=85):
    with Image.open(image_file) as img:
        img.save(output_file, "JPEG", quality=quality)

image_file = "chemin/vers/votre_image.png"
output_file = "chemin/vers/votre_image_compressed.jpg"
compress_image(image_file, output_file)