import streamlit as st
from main_menu import main_menu
from teacher_dashboard import teacher_dashboard
from student_dashboard import student_dashboard

# Custom CSS to set the viewport for mobile devices like the Galaxy S23
st.markdown(
    """
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    @media (max-width: 1080px) {
        .block-container {
            padding: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main function to control the navigation
def main():
    if "page" not in st.session_state:
        st.session_state.page = "main"
    
    if st.session_state.page == "main":
        main_menu()
    elif st.session_state.page == "teacher":
        teacher_dashboard()
    elif st.session_state.page == "student":
        student_dashboard()

if __name__ == "__main__":
    main()
