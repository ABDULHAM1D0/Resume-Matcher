from dotenv import load_dotenv
from AI_matcher import ResumeMatcher
import os
import streamlit as st
from preprocessing import Preprocessor

st.set_page_config("AI Resume Matcher", layout="centered")
st.write("Upload your resume and job description to see how well they matched")

resume_file = st.file_uploader("Upload your resume", type=["pdf", "docx", "txt"])
job_text = st.text_area("Enter Job Description")
# Load .env file
load_dotenv()
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("API_KEY_SECRET")

resume_matcher = ResumeMatcher(api_url=API_URL, api_key=API_KEY)
preprocessor = Preprocessor()

if resume_file and job_text:
    cv_example = preprocessor.extract_text(resume_file)
    jd_example = job_text

    prompt = f"""
    You are an expert recruiter. Compare the following Job Description with the CV.

    1. Return a similarity score as a percentage (0–100%).
    2. Make sure the score reflects how well the CV matches the JD.
    3. Provide a short explanation of the main matched and missing skills.

    Job Description:
    {jd_example}

    CV:
    {cv_example}

    Format your response as:
    Similarity: <number>%
    Skills: <comma-separated list of skills>
    """

    st.subheader("Matching..")
    try:
        result_dict = resume_matcher.comparing(prompt)
        st.success(f'Match Score: **{result_dict["score"]}%**')
        for skill in result_dict["skills"]:
            st.success(skill)
    except Exception as e:
        st.error("Failed to compare")
        st.exception(e)

# print("--- Similarity Result ---")
# print(f"Score: {result_dict['score']}%")
# print("Extracted Skills:", result_dict['skills'])
# print("Raw Output:", result_dict.get("raw_output"))  # helpful for debugging
