import streamlit as st

def show_download_button(text):
    st.download_button("Download Suggestions", text, file_name="optimized_resume.txt")

def show_error(msg):
    st.error(f"⚠️ {msg}")

mode = st.sidebar.toggle("🌙 Dark Mode", value=True)
if mode:
    st.markdown("<style>body { background-color: #0e1117; color: white; }</style>", unsafe_allow_html=True)


import base64
import streamlit as st

def show_pdf(file):
    try:
        base64_pdf = base64.b64encode(file.read()).decode("utf-8")
        pdf_display = f"""
            <iframe src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="600" type="application/pdf"></iframe>
        """
        return pdf_display
    except Exception as e:
        st.warning(f"Could not render PDF: {e}")
        return "❌ Could not preview file"
