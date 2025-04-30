import markdown
import pdfkit
import os
import nbconvert
import nbformat
from pathlib import Path

def convert_notebook_to_html(notebook_path):
    """Convert a Jupyter notebook to HTML."""
    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Configure the HTML exporter
        html_exporter = nbconvert.HTMLExporter()
        html_exporter.template_name = 'classic'
        
        # Convert notebook to HTML
        body, _ = html_exporter.from_notebook_node(nb)
        return body
    except Exception as e:
        print(f"Error converting notebook {notebook_path}: {e}")
        return ""

# Read the markdown file
with open('README.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
readme_html = markdown.markdown(markdown_content)

# Find all notebooks
notebooks = [
    'LalitNayyarIIMK_california_housing_analysis_final.ipynb',
    'LalitNayyarIIMK_california_housing_analysis_with_applications.ipynb',
    'LalitNayyarIIMK_california_housing_analysis_v2.ipynb'
]

# Convert each notebook and collect HTML
notebook_html = ""
for notebook in notebooks:
    if os.path.exists(notebook):
        print(f"Converting {notebook}...")
        notebook_html += f"<h1>Notebook: {notebook}</h1>"
        notebook_html += convert_notebook_to_html(notebook)
    else:
        print(f"Notebook not found: {notebook}")

# Combine everything with styling
styled_html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    body {{
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 40px;
    }}
    h1, h2, h3 {{
        color: #2c3e50;
        margin-top: 30px;
    }}
    code {{
        background-color: #f8f9fa;
        padding: 2px 4px;
        border-radius: 4px;
        font-family: Consolas, monospace;
    }}
    pre {{
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
    }}
    .output_area {{
        margin: 10px 0;
        padding: 10px;
        background-color: #f8f9fa;
        border-left: 3px solid #2c3e50;
    }}
    .cell {{
        margin: 20px 0;
        border-bottom: 1px solid #eee;
    }}
    img {{
        max-width: 100%;
        height: auto;
    }}
</style>
</head>
<body>
<h1>California Housing Analysis Project Documentation</h1>
{readme_html}
<hr>
<h1>Notebook Outputs</h1>
{notebook_html}
</body>
</html>
"""

# Save the HTML file
with open('temp.html', 'w', encoding='utf-8') as f:
    f.write(styled_html)

# Convert HTML to PDF
try:
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }
    pdfkit.from_file('temp.html', 'lalitnayyariimkmod3ass.pdf', configuration=config, options=options)
    print("PDF created successfully with notebook outputs!")
except Exception as e:
    print(f"Error creating PDF: {e}")

# Clean up temporary file
if os.path.exists('temp.html'):
    os.remove('temp.html')
