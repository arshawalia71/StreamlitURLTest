import streamlit as st
import main
import hello

def main_app():
    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "main"

    # Check the current page and render the appropriate content
    if st.session_state.page == "hello":
        hello.hello()
        st.title("Hello Page")  # Update the title
    else:
        main.main()
        st.title("Main Page")   # Update the title

if __name__ == "__main__":
    main_app()
