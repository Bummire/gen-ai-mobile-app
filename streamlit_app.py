import streamlit as st

# Function to display the main page with buttons
def main_page():
    st.title("Welcome to the Dashboard App")
    st.write("Please select your role:")

    # Create columns for centering the buttons
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.write("")
    with col2:
        if st.button("Teacher"):
            st.session_state.page = "teacher"
        if st.button("Student"):
            st.session_state.page = "student"
    with col3:
        st.write("")

# Function to display the teacher's dashboard
def teacher_dashboard():
    st.title("Teacher's Dashboard")
    st.write("Welcome to the Teacher's Dashboard!")
    # Add more components and functionality for the teacher's dashboard here
    if st.button("Go Back"):
        st.session_state.page = "main"

# Function to display the student's dashboard
def student_dashboard():
    st.title("Student's Dashboard")
    st.write("Welcome to the Student's Dashboard!")
    # Add more components and functionality for the student's dashboard here
    if st.button("Go Back"):
        st.session_state.page = "main"

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
