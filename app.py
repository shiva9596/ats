from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
# Verify Poppler installation
print("Checking Poppler path...")
os.system("which pdfinfo")

# Explicitly set the Poppler path for Hugging Face Spaces (Linux)
Poppler_Path = "/usr/bin"  # This is the default path for Hugging Face Spaces

import google.generativeai as genai

# Set up API key
genai.configure(api_key="AIzaSyC3STCle_oIovKZE05bJjNq6uCXrowH0Ao")

# Use the correct model
MODEL_NAME = "gemini-1.5-flash-latest"  # OR "gemini-1.5-pro-latest"

# Function to generate a response
def get_gemini_response(prompt, pdf_content, input_text):
    model = genai.GenerativeModel(MODEL_NAME)  # Ensure correct model name
    response = model.generate_content([prompt, pdf_content[0], input_text])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=Poppler_Path)

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


#Streamlit APP
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ", key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    
    
submit1 = st.button("Tell me About the Resume")

#submit2 = st.button("How can I Improvise My Skills")

submit3 = st.button("Percentage Match")    


input_prompt1 = """
 You are an experienced HR with Tech Experiencein the filed of Data Science, Full stack web developement, Big Data Engineering, Devops, Data Analyst, your task is to review
 the provided resume against the job description for these profiles. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full stack web developement,
Big Data Engineering, Devops, Data Analyst and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")