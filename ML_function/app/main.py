from data_preprocessing import Preprocessing
from embeddings import BertEmbedder
import numpy as np
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Resume Matcher function", layout='centered')

st.title("Resume Matcher")
st.write("Upload your resume and job description to see how well they match")

preprocessing = Preprocessing()
embedding = BertEmbedder()

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
job_text = st.text_area("Enter Job Description")

if resume_file and job_text:
    resume_features = preprocessing.process_data(resume_file)
    job_features = preprocessing.taking_feature(job_text)
    print(resume_features)
    print(job_features)
    st.subheader("🔍 Matching...")
    try:
        resume_vec = np.array(embedding.get_embeddings(resume_features))
        job_vec = np.array(embedding.get_embeddings(job_features))

        similarity_score = cosine_similarity(resume_vec, job_vec)

        print(st.success(f"Match Score: **{similarity_score.item() * 100:.2f}%**"))



    except Exception as e:
        st.error("Failed to compute match score")
        st.exception(e)


