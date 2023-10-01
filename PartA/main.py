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

output_placeholder = st.empty()

def perform_ocr(url, option):
    pdf_text = ""
    
    try:
        # Fetch the PDF content from the URL
        response = requests.get(url)
        if response.status_code == 200:
            pdf_content = response.content

            if option == "PyPDF":
                # PyPDF2-based OCR
                pdf_reader = PdfReader(io.BytesIO(pdf_content))
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_text = pdf_text + page.extract_text()

            else: st.error("Please select a package first!")


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
