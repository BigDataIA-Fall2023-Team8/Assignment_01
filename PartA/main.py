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

def perform_pypdf_ocr(pdf_file):
    pdf_text = ""
    # PyPDF2-based OCR
    pdf_reader = PdfReader(io.BytesIO(pdf_file))
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text = pdf_text + page.extract_text()
    return pdf_text

def perform_nougat_ocr(pdf_file):
    try:
        # Perform OCR using Nougat API
        url = "http://127.0.0.1:8503/predict/"
        files = {'file': pdf_file}
        response = requests.post(url, files=files)

        if response.status_code == 200:
            pdf_text = response.text
            # Display the OCR output
            output_placeholder.write("OCR Output (Nougat):")
            output_placeholder.write(pdf_text)
        else:
            st.error(f"Failed to perform OCR (Nougat). Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred (Nougat): {str(e)}")


if st.button("Perform OCR"):
    if url:
        try:
            # Fetch the PDF content from the URL
            response = requests.get(url)
            if response.status_code == 200:
                pdf_content = response.content

                if option == "PyPDF":
                    pdf_text = perform_pypdf_ocr(pdf_content)
                    # Display the OCR output for PyPDF
                    output_placeholder.write("OCR Output (PyPDF):")
                    output_placeholder.write(pdf_text)

                elif option == "Nougat":
                    # Perform OCR using Nougat
                    # Display a loading message while OCR is in progress
                    output_placeholder.write("Performing OCR (Nougat)... Please wait.")
                    perform_nougat_ocr(io.BytesIO(pdf_content))                  

                else:
                    st.error("Please select a package first!")
            else:
                st.error(f"Failed to fetch the PDF from the URL. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a URL.")
