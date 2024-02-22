import streamlit as st

def main():
    st.title("Main Page")
    if st.button("Go to Hello Page"):
        # Set the URL query parameter to navigate to hello.py
        st.experimental_set_query_params(page="hello")

if __name__ == "__main__":
    main()
