import streamlit as st
import requests
import http.client
import urllib.parse

st.title("Welcome to Streamlit - OCR")

import streamlit as st

option = st.selectbox(
   "Which Package would you like to use?",
   ("Nougat","PyPDF"),
   index=None,
   placeholder="Select OCR method...",
)

st.write('You selected:', option)

url = st.text_input('The URL link')

if url:
    # Parse the URL to extract the host and optional port
    url_parts = urllib.parse.urlparse(url)
    host = url_parts.netloc
    port = 80  # Default HTTP port

    # If the URL includes a port, parse it
    if ':' in host:
        host, port = host.split(':')
        port = int(port)

    try:
        # Create an HTTPConnection
        connection = http.client.HTTPConnection(host, port)

        # Send an HTTP GET request
        connection.request('GET', '/')

        # Get the response
        response = connection.getresponse()

        # Print the response status code and content
        st.write(f"Response Status Code: {response.status}")
        st.write("Response Content:")
        st.write(response.read())

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    st.warning("Please enter a URL.")
