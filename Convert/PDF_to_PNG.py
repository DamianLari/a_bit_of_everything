from pdf2image import convert_from_path
#à réparer
def pdf_to_images(pdf_file, output_folder):
    images = convert_from_path(pdf_file)
    for i, image in enumerate(images):
        image.save(f"{output_folder}/page_{i + 1}.png", "PNG")

pdf_file = "Input/InputFiler.pdf"
output_folder = "ImageFolder"
pdf_to_images(pdf_file, output_folder)