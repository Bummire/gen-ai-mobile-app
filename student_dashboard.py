import streamlit as st
import streamlit.components.v1 as components

def student_dashboard():
    """"
    <style> 
        h1 {
            text-align: center;
            color: black;
            font-size: 50px;
        }
    
        h1 {
            text-align: center;
            color: black;
            font-size: 20px;
        }
    </style>
    """
    
    st.markdown(
        """
        <h1>Student's Dashboard</h1>
        <p>You can take your quiz using our fine-tuned AI bot!</p>
        """,
        unsafe_allow_html=True
    )

    # Embedded Relevance AI Agent for Student Use
    iframe_code = '''
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/2988d09a-bb1d-44d7-9d82-08ddd53ab748/share" width="100%" height="800px" frameborder="0"></iframe>'''
    components.html(iframe_code, height=800)
    
    if st.button("Sign out"):
        st.session_state.student_mode = "default"
