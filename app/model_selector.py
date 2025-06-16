import streamlit as st

OPTIMIZATION_OPTIONS = {
    "ATS Keyword Optimizer": "Identify and optimize keywords from the job description for better ATS compatibility.",
    "Experience Section Enhancer": "Rewrite experience sections to include measurable impact aligned with job requirements.",
    "Skills Hierarchy Creator": "Organize and highlight skills based on importance to the job.",
    "Professional Summary Crafter": "Craft a strong summary that aligns with the job.",
    "Education Optimizer": "Improve education section by highlighting relevant degrees or certifications.",
    "Technical Skills Showcase": "Make technical skills more prominent based on the job.",
    "Career Gap Framing": "Handle resume gaps with positive framing and context."
}

def sidebar_logo():
    st.sidebar.image("assets/logo.png", width=150)

def file_uploader():
    return st.sidebar.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])

def job_inputs():
    return st.text_input("Job Title"), st.text_area("Job Description")

def optimization_selector():
    return st.selectbox("Choose Optimization Type", list(OPTIMIZATION_OPTIONS.keys()))

def llm_model_selector():
    return st.selectbox("LLM Model", [
        "gpt-3.5-turbo",
        "gpt-4",
        "gpt-4-0613",
        "gpt-4-1106-preview",
        "gpt-4o",
        "claude-3-haiku-20240307",
        "claude-3-sonnet-20240229",
        "claude-3-opus-20240229"
    ])
