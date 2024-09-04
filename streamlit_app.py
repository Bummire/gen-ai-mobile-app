import streamlit as st

def main_menu():
    # Add custom CSS for the background image
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://i.ibb.co/7pMMJpJ/sample-image.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        .stButton>button {
            background-color: rgba(255, 255, 255, 0.8);
            color: black;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <h1 style="text-align: center;">AI Cybered Solutions</h1>
        <p style="text-align: center;">A Generative AI adaptive learning and teaching tool for <br>cybersecurity education</p>
        <h3 style="text-align: center;"><br>Sign in as<br></h3>
        """,
        unsafe_allow_html=True
    )

    # Create a single row with two columns for the buttons centered on the page
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Teacher"):
            st.session_state.page = "teacher"
    with col2:
        if st.button("Student"):
            st.session_state.page = "student"
    
    st.markdown("""
    <style>
    .stButton>button {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    if "page" not in st.session_state:
        st.session_state.page = None
    
    if st.session_state.page is None:
        main_menu()
    elif st.session_state.page == "teacher":
        # Handle teacher page content
        st.write("Teacher Page")
    elif st.session_state.page == "student":
        # Handle student page content
        st.write("Student Page")

if __name__ == "__main__":
    main()
