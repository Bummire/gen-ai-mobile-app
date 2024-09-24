import streamlit as st
from teacher_dashboard import teacher_dashboard
from student_dashboard import student_dashboard

def main_menu():
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
            background-image: url("https://i.ibb.co/YyGdRxq/image.png");
            background-size: cover;
            background-position: center;
            overflow: hidden;
        }

        /* Hopefully it prevents scrolling on mobile devices */
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
            text-align: center;
        }

        .button-container {
            display: flex;
            flex-direction: column;
            justify-content: flex-end;  /* Align buttons at the bottom */
            height: 25vh;  /* Take up most of the screen's height */
            align-items: center;
        }

        .stButton>button {
            width: 95%;  /* Button takes up 80% of the screen width */
            margin: 10px;
            padding: 15px;
            font-size: 20px;
            background-color: rgba(255, 255, 255, 0.3);  /* Make the buttons slightly transparent */
            border-radius: 25px;
            color: white;  
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Shadow */
        }
    
        h1 {
            margin-top: 30px;
            font-size: 50px;
            color: white;
        }

        p {
            font-size: 20px;
            color: white;
        }

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Center the text at the top
    st.markdown(
        """
        <h1>CyberEd</h1>
        <p>Level Up Your Cyber Skills with AI</p>
        """,
        unsafe_allow_html=True
    )

    # Container to hold buttons at the bottom
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    if st.button("Teacher"):
        st.session_state.page = "Teacher"
    if st.button("Student"):
        st.session_state.page = "Student"

    st.markdown('</div>', unsafe_allow_html=True)

def main():
    if "page" not in st.session_state:
        st.session_state.page = None

    if st.session_state.page is None:
        main_menu()  # Display the menu with the background
    elif st.session_state.page == "Teacher":
        teacher_dashboard()
    elif st.session_state.page == "Student":
        student_dashboard()

if __name__ == "__main__":
    main()
