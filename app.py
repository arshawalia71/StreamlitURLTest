import streamlit as st
import main
import hello

def main_app():
    # Get the URL query parameters
    url_params = st.experimental_get_query_params()

    # Check if the "page" parameter is set to "hello"
    if "page" in url_params and url_params["page"][0] == "hello":
        # Display the content for the hello.py page
        hello.hello()
    else:
        # Display the content for the main.py page
        main.main()

if __name__ == "__main__":
    main_app()
