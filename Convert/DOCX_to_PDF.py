from docx import Document
from fpdf import FPDF
# à réparer
def docx_to_pdf(docx_file, pdf_file):
    doc = Document(docx_file)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, para.text)
    
    pdf.output(pdf_file)

docx_file = "Input/InputFile.docx"
pdf_file = "Output/OutputFile.pdf"
docx_to_pdf(docx_file, pdf_file)