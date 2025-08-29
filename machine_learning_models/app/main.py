from embedder import Embedder
from prediction import Predict
import numpy as np
from preprocessing import Preprocessing
import streamlit as st

st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("Resume Matcher")
st.write("Upload your resume and job description to see how well they match.")

processing = Preprocessing()
embedding = Embedder()
model = Predict()

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
job_text = st.text_area("Paste Job Description")

if resume_file and job_text:
    resume_text = processing.extract_text(resume_file)
    print(resume_text)
    print(job_text)
    st.subheader("🔍 Matching...")
    try:
        # resume_vec = get_embeddings([resume_text])[0]
        # job_vec = get_embeddings([job_text])[0]
        resume_vec = embedding.get_embeddings(resume_text)
        job_vec = embedding.get_embeddings(job_text)
        print(resume_vec)
        print(job_vec)
        combined = np.hstack((resume_vec, job_vec))
        score = model.predict_match_score(combined)

        st.success(f"Match Score: **{score:.2f}%**")

    except Exception as e:
        st.error("Failed to compute match score.")
        st.exception(e)
