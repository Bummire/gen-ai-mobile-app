import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

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

        h2 {
            color: black;
            font-size: 20px;
            text-align: center;
        }

        h3 {
            color: black;
            font-size: 20px;
        }

        p {
            color: black;
            font-size: 15px;
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

        /* Custom styling for the expander box */
        div.stExpander {
            background-color: white;
            border: 1px solid #b7b7c1;
            border-radius: 5px;
            margin-left: 9px;
            margin-right: 9px;
        }

        /* Streamlit class name of the div that holds the expander's title*/
        .st-emotion-cache-uef7qa p {
            font-size: 16px;
            color: black;
            font-weight: bold;
        }

        /* Fancier styling with color sweep on click */
        div.stDownloadButton > button {
            margin-top: 7px;
            background: linear-gradient(120deg, #b7b7c1, #ffffff);
            color: black;
            font-size: 12px;
            padding: 10px 20px;
            margin-left: 8px;
            border-radius: 30px;
            border: 2px solid #b7b7c1;
            cursor: pointer;
            transition: background-position 0.4s ease;  /* Smooth transition */
            background-size: 200%;  /* Double the background size for animation */
            background-position: right;  /* Start with background aligned to the right */
        }

        div.stDownloadButton > button:hover {
            background-position: left;  /* Move gradient to the left on hover */
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);  /* Slightly larger shadow on hover */
        }

        div.stDownloadButton > button:active {
            background-position: left;  /* Move gradient to the left on click */
            transform: translateY(4px);  /* Button moves down slightly on click */
        }

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.markdown(
        """
        <h1>Teacher's Dashboard</h1>
        <h2>Our fine-tuned agent is capable of generating quizzes from your inputs!</h2>
        """,
        unsafe_allow_html=True
    )

    # Create an expandable "Setup" section
    with st.expander("Add Student Guide", expanded=False):  # Keep the expander title empty
        
        # Create a sample CSV for download
        sample_data = pd.DataFrame({
            "id": ["4422", "2244"],
            "name-": ["John Doe", "Jane Smith"]
        })
        
        csv_data = sample_data.to_csv(index=False).encode('utf-8')

        # Button to download the CSV file
        st.download_button(label="Download Student Template File", data=csv_data, file_name="Student_Template.csv", mime='text/csv')
        
        st.markdown(
            """
            <h3>Instructions:</h3>
            <p>- Step 1: Download the template file above.</p>
            <p>- Step 2: Add new students based on template.</p>
            <p>- Step 3: Drag and drop the file edited file into the message bar below, then press submit.</p>
            """,
            unsafe_allow_html=True
        )

    
    # Embedded Relevance AI Agent for Teacher
    iframe_code = '''
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/ba215e62-16f1-4225-bbcd-4625feb417f4/share" width="100%" height="800px" frameborder="0"></iframe>'''
    components.html(iframe_code, height=800)

    if st.button("Sign out"):
        st.session_state.page = None
