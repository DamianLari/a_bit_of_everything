import markdown
import sys

def md_to_html(md_file, html_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        text = file.read()
        html = markdown.markdown(text)
    
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html)

# Exemple d'utilisation
md_file = "Input/InputFile.md"
html_file = "Output/OutputFile.html"
md_to_html(md_file, html_file)