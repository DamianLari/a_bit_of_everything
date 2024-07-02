from weasyprint import HTML
#à réparer
def html_to_pdf(html_file, pdf_file):
    HTML(html_file).write_pdf(pdf_file)

# Exemple d'utilisation
html_file = "Input/InputFile.html"
pdf_file = "Output/OutputFile.pdf"
html_to_pdf(html_file, pdf_file)