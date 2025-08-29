import pdfplumber
import docx

class Preprocessing:

    def extract_text(self, file):
        if file.name.endswith('.pdf'):
            with pdfplumber.open(file) as pdf:
                return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        elif file.name.endswith('.docx'):
            doc = docx.Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        elif file.name.endswith('.txt'):
            return str(file.read(), 'utf-8')
        else:
            return ""