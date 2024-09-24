import streamlit as st
import streamlit.components.v1 as components

def teacher_dashboard():
    # Apply background image only on the main menu
    page_bg_img = """
    <style> 
        /* Meta tag to set viewport for responsive design */
        @viewport {
            width: device-width;
            initial-scale: 1;
            user-scalable=no;
        }

        [data-testid="stApp"] {
            background-color: #ffffff;
            opacity: 1;
            background-image:  linear-gradient(#b7b7c1 1.4000000000000001px, transparent 1.4000000000000001px), linear-gradient(to right, #b7b7c1 1.4000000000000001px, #ffffff 1.4000000000000001px);
            background-size: 28px 28px;
        }

        h1 {
            text-align: center;
            color: black;
            font-size: 50px;
        }

        p {
            text-align: center;
            color: black;
            font-size: 20px;
        }

        /* Custom styling for the button */
        div.stButton > button {
            background-color: white;
            border: 1px solid #b7b7c1;
            color: black;
            font-size: 10px;
            margin-left: 8px;
            border-radius: 5px;
            cursor: pointer;
        }

        div.stButton > button:hover {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);  /* Shadow */
        }

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown(
        """
        <h1>Teacher's Dashboard</h1>
        <p>Our fine-tuned agent is capable of generating quizzes from your inputs!</p>
        """,
        unsafe_allow_html=True
    )
    
    # Embedded Relevance AI Agent for Teacher
    iframe_code = '''
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/2988d09a-bb1d-44d7-9d82-08ddd53ab748/share" width="100%" height="800px" frameborder="0"></iframe>'''
    components.html(iframe_code, height=800)

    if st.button("Sign out"):
        st.session_state.page = None
