# CV and Job Description Matcher
- This project is a CV and Job Description Matching Model that calculates the similarity between a candidate's CV and a job description.
- It is built in Python using NLP and machine learning libraries and provides a similarity score to help assess candidate-job fit.

## Features
- Supports input files in DOCX, PDF, or plain text formats.
- Uses spaCy, Sentence-Transformers, and scikit-learn to process text and compute similarity scores.
- Model can be saved and loaded with joblib for easy reuse.

## Installation
- No special installation is required beyond having Python and the following libraries:
```bash
pip install spacy scikit-learn sentence-transformers python-docx PyPDF2
```

## Usage
- Load the saved model using joblib.
- Provide a CV and a job description as input.
- Get a similarity score between 0 and 100.

## Example:
```python
from joblib import load
model = load('cv_job_matcher_model.joblib')
similarity_score = model.predict(cv_text, job_description_text)
print(f"Similarity Score: {similarity_score}")
```

## How it Works
- Extract text from CV and job description files.
- Preprocess text using spaCy (tokenization, lemmatization, stopword removal).
- Convert text to embeddings using Sentence-Transformers.
Compute similarity scores with scikit-learn metrics.
