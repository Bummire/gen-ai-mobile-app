import streamlit as st
import requests
import json
import streamlit.components.v1 as components
import random

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
    st.write("<h3>AI Generated Quiz</h3>", unsafe_allow_html=True)
    # Add more components and functionality for the teacher's dashboard here

    if st.button("Go Back"):
        st.session_state.page = "main"

# Function to trigger Relevance AI app
def trigger_relevance_ai(file_url):
    api_key = 'sk-YTI0ZjlkY2ItNWQ1ZC00ZDIxLThlMGYtZTVhZTUxYzQxMTc3'  # Replace with your API key
    endpoint = 'https://api-f1db6c.stack.tryrelevance.com/latest/studios/75ddd01a-1841-4267-abfd-0297ad3f83fe/trigger_limited'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'sk-YTI0ZjlkY2ItNWQ1ZC00ZDIxLThlMGYtZTVhZTUxYzQxMTc3'
    }

    payload = {
        'params': {
            'subject_file_urls': [],
            'file_url': file_url
        },
        'project': '8cf8ab1430e6-45f0-9431-31e53339530f'
    }

    iframe_code = '''
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/1d783e42-566a-4936-bd21-1ac9060c802e/share" width="100%" height="800px" frameborder="0"></iframe>'''

    components.html(iframe_code, height=800)

    try:
        response = requests.post(endpoint, headers=headers, data=json.dumps(payload))
        response_data = response.json()
        return response_data
    except Exception as e:
        st.error(f"Error calling Relevance AI API: {str(e)}")

# Function to display the student's dashboard
def student_dashboard():
    st.title("Student's Dashboard")
    
    if "student_mode" not in st.session_state:
        st.session_state.student_mode = "default"
    
    # Student Dashboard with 3 options, login, create and go back (returns user to main screen)
    if st.session_state.student_mode == "default":
        st.write("Please choose an option:")
        if st.button("Login"):
            st.session_state.student_mode = "login"
        if st.button("Create User"):
            st.session_state.student_mode = "create"
        if st.button("Go Back"):
            st.session_state.page = "main"
    
    # Login screen where user can input their existing ID
    elif st.session_state.student_mode == "login":
        login_id = st.text_input("Enter your 7-digit ID", max_chars=7)
        if len(login_id) == 7 and login_id.isdigit():
            st.success("Logged in successfully!")
            st.session_state.student_mode = "logged_in"
        elif len(login_id) > 0:
            st.error("ID must be 7 digits long")
        if st.button("Go Back"):
            st.session_state.student_mode = "default"
    
    # A new ID for student is generated (7 digits), which they can use to login
    elif st.session_state.student_mode == "create":
        new_id = str(random.randint(1000000, 9999999))
        st.markdown(f"Your new ID is: **{new_id}**", unsafe_allow_html=True)
        st.write("Please save your ID somewhere safe for future usage!")
        if st.button("Login"):
            st.session_state.student_mode = "login"
    
    # Once login is successful, the Relevance AI Agent appears
    elif st.session_state.student_mode == "logged_in":
        iframe_code = '''
        <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/75ea7fba-abc0-4be4-8069-7a784ce68ff5/share" width="100%" height="800px" frameborder="0"></iframe>'''
        components.html(iframe_code, height=800)
        if st.button("Go Back"):
            st.session_state.student_mode = "default"


# Main function to control the navigation
def main():
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
