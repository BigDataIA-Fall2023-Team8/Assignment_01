import streamlit as st
import requests
import http.client
import urllib.parse
import io
import PyPDF2
from PyPDF2 import PdfReader

st.title("Welcome to Streamlit - OCR")

option = st.selectbox(
   "Which Package would you like to use?",
   ("Nougat","PyPDF"),
   index=None,
   placeholder="Select OCR method...",
)

st.write('You selected:', option)

url = st.text_input('The PDF URL Link')

pdf_text = ""
# if url:
#     # Parse the URL to extract the host and optional port
#     url_parts = urllib.parse.urlparse(url)
#     host = url_parts.netloc
#     port = 80  # Default HTTP port

#     # If the URL includes a port, parse it
#     if ':' in host:
#         host, port = host.split(':')
#         port = int(port)

#     try:                                                    
#         # Create an HTTPConnection
#         connection = http.client.HTTPConnection(host, port)

#         # Send an HTTP GET request
#         connection.request('GET', '/')

#         # Get the response
#         response = connection.getresponse()

#         # Print the response status code and content
#         st.write(f"Response Status Code: {response.status}")
#         st.write("Response Content:")
#         st.write(response.read())

#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")
# else:
#     st.warning("Please enter a URL.")

output_placeholder = st.empty()

def perform_ocr(url, option):
    try:
        # Fetch the PDF content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            pdf_content = response.content

            if option == "PyPDF":
                # PyPDF2-based OCR
                pdf_reader = PdfReader(io.BytesIO(pdf_content))
                pdf_text = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_text += page.extract_text()

            # Display the OCR output
            output_placeholder.write("OCR Output:")
            output_placeholder.write(pdf_text)

        else:
            st.error(f"Failed to fetch the PDF from the URL. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

if st.button("Perform OCR"):
    if url:
        # Display a loading message while OCR is in progress
        output_placeholder.write("Performing OCR... Please wait.")
        
        # Perform OCR and display the result
        perform_ocr(url, option)
    else:
        st.warning("Please enter a URL.")
    st.warning("Please enter a URL.")
