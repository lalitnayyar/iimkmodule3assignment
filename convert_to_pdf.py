import markdown
import pdfkit
import os

# Read the markdown file
with open('README.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(markdown_content)

# Add some basic styling
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
    }}
    code {{
        background-color: #f8f9fa;
        padding: 2px 4px;
        border-radius: 4px;
    }}
    pre {{
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
    }}
</style>
</head>
<body>
{html_content}
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
    pdfkit.from_file('temp.html', 'lalitnayyariimkmod3ass.pdf', configuration=config)
    print("PDF created successfully!")
except Exception as e:
    print(f"Error creating PDF: {e}")

# Clean up temporary file
if os.path.exists('temp.html'):
    os.remove('temp.html')
