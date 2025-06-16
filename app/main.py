import streamlit as st
st.set_page_config(page_title="Smart Resume Optimizer", layout="wide")
import processor
import ui
import optimizer
import compare
import utils

ui.sidebar_logo()
file = ui.file_uploader()

# 👇 Ask for API Key
st.sidebar.subheader("🔐 API Key")
user_api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

if file:
    try:
        # Read and show PDF preview
        st.markdown("### 📄 Resume Preview")
        st.markdown(utils.show_pdf(file), unsafe_allow_html=True)

        # Parse resume text
        resume_text = processor.parse_resume(file)

        # Job input
        job_title, job_desc = ui.job_inputs()

        # Optimization type + LLM selection
        optimization_type = ui.optimization_selector()
        selected_model = ui.llm_model_selector()

        # Button to trigger optimization
        if st.button("🚀 Optimize Resume"):
            if not user_api_key:
                st.error("Please enter your OpenAI API key.")
                st.stop()

            with st.spinner("Generating optimized suggestions..."):
                result = optimizer.optimize_resume(
                    text=resume_text,
                    prompt=ui.OPTIMIZATION_OPTIONS[optimization_type],
                    job_title=job_title,
                    job_description=job_desc,
                    gen_model=selected_model,
                    api_key=user_api_key  
                )

            if result:
                st.subheader("AI Suggestions ✨")
                st.markdown(result)
                utils.show_download_button(result)

                if st.checkbox("🧾 Show Before vs After Comparison"):
                    diff = compare.diff_text(resume_text, result)
                    st.text_area("Comparison", diff, height=300)

    except Exception as e:
        utils.show_error(str(e))
if st.button("🧠 Generate Tailored Resume"):
    with st.spinner("Generating tailored resume..."):
        tailored = optimizer.generate_tailored_resume(
            text=resume_text,
            job_title=job_title,
            job_description=job_desc,
            model=selected_model
        )
        st.subheader("Tailored Resume")
        st.markdown(tailored)
        utils.show_download_button(tailored)
