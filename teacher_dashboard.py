import streamlit as st
import streamlit.components.v1 as components

def teacher_dashboard():
    st.markdown(
        """
        <h1 style="text-align: center;">Teacher's Dashboard</h1>
        <h3 style="text-align: center;">Chatbot Agent</h3>
        <p style="text-align: center;">Our fine-tuned agent is capable of generating quizzes from your inputs!</p>
        """,
        unsafe_allow_html=True
    )
    
    # Embedded Relevance AI Agent for Teacher
    iframe_code = '''
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/2988d09a-bb1d-44d7-9d82-08ddd53ab748/share" width="100%" height="800px" frameborder="0"></iframe>'''
    components.html(iframe_code, height=800)

    if st.button("Sign out"):
        st.session_state.page = "main"
