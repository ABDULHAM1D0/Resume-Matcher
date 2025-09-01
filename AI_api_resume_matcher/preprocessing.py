import pdfplumber
import docx

class Preprocessor:
    def extract_text(self, file):
        if file.name.endswith("pdf"):
            try:
                with pdfplumber.open(file) as pdf:
                    return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()]).strip()

            except Exception as e:
                print("Error reading PDF", e)
                return None

        elif file.name.endswith("docx"):
            doc = docx.Document(file)
            return "\n".join([para.text for para in doc.paragraphs]).strip()

        elif file.name.endswith("txt"):
            content = file.read()
            if isinstance(content, bytes):
                return content.decode("utf-8").strip()
            return content.strip()

        else:
            return None