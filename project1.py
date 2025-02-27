import subprocess
import sys

# Install missing dependencies
def install_packages():
    packages = ["PyPDF2", "python-docx"]
    for package in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", package])

install_packages()


import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import io  

st.title("PDF to Word Converter")
st.write("Upload your PDF here:")
uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file is not None:
    pdf = PdfReader(uploaded_file)  # Load the PDF
    st.write("PDF successfully uploaded")

    num_pages = len(pdf.pages)  # ✅ Fix: Use `pages`, not `Pages`
    st.write(f"Number of Pages: {num_pages}")

    doc = Document()

    for page in pdf.pages:  # ✅ Loop through pages correctly
        text = page.extract_text() or ""  # ✅ Handle NoneType
        doc.add_paragraph(text)

    word_io = io.BytesIO()
    doc.save(word_io)
    word_io.seek(0)

    st.download_button(
        label="Download Converted File",
        data=word_io,
        file_name="Converted.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
else:
    st.warning("Please upload a PDF file.")
