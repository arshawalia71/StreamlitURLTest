import streamlit as st

def main():
    st.title("Main Page")
    if st.button("Go to Hello Page"):
        # Set the session state variable to navigate to hello.py
        st.session_state.page = "hello"

if __name__ == "__main__":
    main()
