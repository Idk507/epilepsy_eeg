import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from fpdf import FPDF

# Load the trained model using joblib
loaded_model = joblib.load('pipelinemodel.pkl')

# Function to preprocess input data and make predictions
def predict_epilepsy(input_data):
    # Preprocess the input data using the same scaler used during training
    input_data = sc.transform(input_data)
    
    # Make predictions
    predictions = loaded_model.predict(input_data)
    
    return predictions

# Streamlit app settings
st.set_page_config(
    page_title="Epilepsy Prediction",
    page_icon="🧠",
    layout="wide"
)



# Streamlit app title and introduction

# Streamlit app title and introduction
st.title('Epilepsy Prediction App')

st.write('Welcome to the Epilepsy Prediction App! Enter patient information and upload a CSV file for prediction.')
# Centered image
st.image("eeg.png",width=500)

st.sidebar.header('Patient Information')
patient_name = st.sidebar.text_input('Patient Name')
patient_age = st.sidebar.number_input('Patient Age', min_value=1, max_value=100, value=30)
patient_gender = st.sidebar.selectbox('Patient Gender', ['Male', 'Female', 'Other']) 

# Display predictions and download as PDF
if st.sidebar.file_uploader("Upload a CSV file", type=["csv"]):
    # Assuming data preprocessing and prediction here
    predictions = predict_epilepsy(input_data)
    
    # Create a PDF report with user information and results
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Epilepsy Prediction Report", align="C", ln=True)
            self.cell(0, 10, "", ln=True)  # Add empty line
        
        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Page {self.page_no()}", align="C")

        def chapter_title(self, title):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, title, 0, 1)
            self.ln(10)

        def chapter_body(self, body):
            self.set_font("Arial", "", 12)
            self.multi_cell(0, 10, body)
            self.ln()

    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title("Patient Information")
    pdf.chapter_body(f"Name: {patient_name}")
    pdf.chapter_body(f"Age: {patient_age} years")
    pdf.chapter_body(f"Gender: {patient_gender}")
    pdf.ln(10)
    pdf.chapter_title("Epilepsy Prediction")
    if predictions[0] == 1:
        pdf.chapter_body("You have symptoms of Epilepsy.🧠")
        pdf.chapter_body("Please approach a doctor for further screening and diagnosis.")
        pdf.chapter_body("Prevention Measures:")
        pdf.chapter_body("1. Get enough sleep and maintain a regular sleep schedule.")
        pdf.chapter_body("2. Manage stress through relaxation techniques.")
        pdf.chapter_body("3. Avoid excessive alcohol consumption.")
        pdf.chapter_body("4. Follow a balanced diet and stay hydrated.")
        pdf.chapter_body("5. Take medication as prescribed.")
        pdf.chapter_body("6. Wear a medical alert bracelet.")
        pdf.chapter_body("7. Avoid seizure triggers.")
    else:
        pdf.balloons()
        pdf.chapter_body("You are safe and have no symptoms of Epilepsy. Take care of your health.")
    
    # Save the PDF
    pdf_file_path = "epilepsy_report.pdf"
    pdf.output(pdf_file_path)

    # Provide a download link for the PDF
    st.sidebar.markdown(
        f"Download the Epilepsy Prediction Report: [Epilepsy Report PDF]({pdf_file_path})"
    )
