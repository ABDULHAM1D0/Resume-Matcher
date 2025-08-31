import pdfplumber
import docx
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag


class Preprocessing:
    def extract_text(self, file):
        if file.name.endswith('.pdf'):
            try:
                with pdfplumber.open(file) as pdf:
                    return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()]).strip()
            except Exception as e:
                print(f"Error reading PDF: {e}")
                return ""
        elif file.name.endswith('.docx'):
            doc = docx.Document(file)
            return "\n".join([para.text for para in doc.paragraphs]).strip()
        elif file.name.endswith('.txt'):
            content = file.read()
            if isinstance(content, bytes):
                return content.decode("utf-8").strip()
            return content.strip()
        else:
            return ""

    def taking_feature(self, text):
        text = text.lower()
        text = re.sub('[^a-zA-Z]', ' ', text)
        sentences = sent_tokenize(text)
        stop_words = set(stopwords.words("english"))

        features_list = []
        for sentence in sentences:
            if any(criteria in sentence for criteria in ["skills", "education"]):
                words = word_tokenize(sentence)
                words = [word for word in words if word not in stop_words]
                tagged = pos_tag(words)
                filtered = [word for word, tag in tagged if tag not in ['DT', 'IN', 'TO', 'PRP', 'WP']]
                features_list.extend(filtered)

        return " ".join(features_list)

    def process_data(self, data):
        text = self.extract_text(data)
        features_text = self.taking_feature(text)
        return features_text