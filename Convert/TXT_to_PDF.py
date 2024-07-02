from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file, pdf_file):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    width, height = letter

    with open(txt_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    x = 50
    y = height - 50
    line_height = 12

    for line in lines:
        c.drawString(x, y, line.strip())
        y -= line_height
        if y < 50:  
            c.showPage()
            y = height - 50

    c.save()

# Exemple d'utilisation
txt_file = "Input/InputFile.txt"
pdf_file = "Output/OutputFile.pdf"
txt_to_pdf(txt_file, pdf_file)
