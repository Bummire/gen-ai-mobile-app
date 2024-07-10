import streamlit as st
import requests
import json

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/3RTsjV85/081aed2e7ddc029f940021ddb22145fc.jpg");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Function to apply custom CSS
def apply_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: white;
            color: black;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: black;
            font-size: 36px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        h2 {
            color: black;
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 16px;
        }
        h3 {
            color: black;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to display the main page with buttons
def main_page():
    st.title("Generative AI Learning App")

    # Centering the "Please select your role" text
    st.markdown("<h3>Sign in as</h3>", unsafe_allow_html=True)

    # Create columns for side-by-side buttons centered on the page
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col2:
        if st.button("Teacher"):
            st.session_state.page = "teacher"
    with col4:
        if st.button("Student"):
            st.session_state.page = "student"

# Function to display the teacher's dashboard
def teacher_dashboard():
    st.title("Teacher's Dashboard")
    st.write("<h3>Create a quiz</h3>", unsafe_allow_html=True)
    # Add more components and functionality for the teacher's dashboard here

    # File upload section
    uploaded_file = st.file_uploader("Upload a file")

    if uploaded_file is not None:
        file_url = "https://example.com/uploaded_file.pdf"  # Replace with actual file URL
        result = trigger_relevance_ai(file_url)
        st.json(result)

    if st.button("Go Back"):
        st.session_state.page = "main"
# Function to trigger Relevance AI app
def trigger_relevance_ai(file_url):
    api_key = 'YOUR_API_KEY'  # Replace with your API key
    endpoint = 'https://api-f1db6c.stack.tryrelevance.com/latest/studios/75ddd01a-1841-4267-abfd-0297ad3f83fe/trigger_limited'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': api_key
    }

    payload = {
        'params': {
            'subject_file_urls': [],
            'file_url': file_url
        },
        'project': '8cf8ab1430e6-45f0-9431-31e53339530f'
    }

    try:
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        return response_data
    except Exception as e:
        st.error(f"Error calling Relevance AI API: {str(e)}")

# Function to display the student's dashboard
def student_dashboard():
    st.title("Student's Dashboard")
    st.write("Welcome to the Student's Dashboard!")
    # Add more components and functionality for the student's dashboard here
    if st.button("Go Back"):
        st.session_state.page = "main"

# Main function to control the navigation
def main():
    apply_custom_css()
    if "page" not in st.session_state:
        st.session_state.page = "main"
    
    if st.session_state.page == "main":
        main_page()
    elif st.session_state.page == "teacher":
        teacher_dashboard()
    elif st.session_state.page == "student":
        student_dashboard()

if __name__ == "__main__":
    main()
