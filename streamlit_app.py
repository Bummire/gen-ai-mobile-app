import streamlit as st
import streamlit.components.v1 as components
import random

# Function to display the main page with buttons
def main_page():
    st.markdown(
        """
        <h1 style="text-align: center;">Generative AI Learning App</h1>
        <h3 style="text-align: center;">Sign in as</h3>
        """,
        unsafe_allow_html=True
    )

    # Create a single row with two columns for the buttons centered on the page
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])

    with col2:
        if st.button("Teacher"):
            st.session_state.page = "teacher"
    with col4:
        if st.button("Student"):
            st.session_state.page = "student"

# Function to display the teacher's dashboard
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
    <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/1d783e42-566a-4936-bd21-1ac9060c802e/share" width="100%" height="800px" frameborder="0"></iframe>'''
    components.html(iframe_code, height=800)

    if st.button("Go Back"):
        st.session_state.page = "main"


# Function to display the student's dashboard
def student_dashboard():
    st.markdown(
        """
        <h1 style="text-align: center;">Student's Dashboard</h1>
        """,
        unsafe_allow_html=True
    )

    if "student_mode" not in st.session_state:
        st.session_state.student_mode = "default"
    
    # Student Dashboard with 3 options, login, create, and go back (returns user to main screen)
    if st.session_state.student_mode == "default":
        st.markdown(
            """
            <p style="text-align: center;">Please choose an option:</p>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        
        with col2:
            if st.button("Login"):
                st.session_state.student_mode = "login"
        with col3:
            if st.button("Create User"):
                st.session_state.student_mode = "create"
        with col4:
            if st.button("Go Back"):
                st.session_state.page = "main"

    
    # Login screen where user can input their existing ID
    elif st.session_state.student_mode == "login":
        st.markdown(
            """
            <h3 style="text-align: center;">Enter your 7-digit ID</h3>
            """,
            unsafe_allow_html=True
        )
        login_id = st.text_input("", max_chars=7)

        if len(login_id) == 7 and login_id.isdigit():
            st.success("Logged in successfully!")
            
            # Create a single row with two columns for the buttons
            col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])  # Adjust column widths as needed
            
            with col2:
                if st.button("Proceed"):
                    st.session_state.student_mode = "logged_in"
                    
            with col4:
                if st.button("Go Back"):
                    st.session_state.student_mode = "default"
                
        elif len(login_id) > 0:
            st.error("ID must be 7 digits long")
    
    # A new ID for student is generated (7 digits), which they can use to login
    elif st.session_state.student_mode == "create":
        st.markdown(
            """
            <h3 style="text-align: center;">Your new ID is:</h3>
            """,
            unsafe_allow_html=True
        )
        new_id = str(random.randint(1000000, 9999999))
        st.markdown(f"<p style='text-align: center;'><strong>{new_id}</strong></p>", unsafe_allow_html=True)
        st.markdown(
            """
            <p style="text-align: center;">Please save your ID somewhere safe for future usage!</p>
            """,
            unsafe_allow_html=True
        )

        # Utilised when centering buttons
        col1, col2, col3 = st.columns([1, 1, 1])  # Adjust column proportions if necessary
        
        with col2:  # Middle column
            if st.button("Login"):
                st.session_state.student_mode = "login"
    
    # Once login is successful, the Relevance AI Agent appears
    elif st.session_state.student_mode == "logged_in":
        st.markdown(
            """
            <p style="text-align: center;">You can take your quiz using our fine-tuned AI bot!</p>
            """,
            unsafe_allow_html=True
        )
        
        # Embedded Relevance AI Agent for Student Use
        iframe_code = '''
        <iframe src="https://app.relevanceai.com/agents/f1db6c/8cf8ab1430e6-45f0-9431-31e53339530f/1d783e42-566a-4936-bd21-1ac9060c802e/share" width="100%" height="800px" frameborder="0"></iframe>'''
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
