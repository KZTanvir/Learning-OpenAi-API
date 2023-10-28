from docx import Document

def convert_docx_to_text(docx_path, output_path):
    doc = Document(docx_path)
    paragraphs = [p.text for p in doc.paragraphs]
    text = '\n'.join(paragraphs)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

# Example usage
docx_file = '50test.docx'  # Path to your input DOCX file
output_file = 'output.txt'  # Path to the output text file

convert_docx_to_text(docx_file, output_file)
