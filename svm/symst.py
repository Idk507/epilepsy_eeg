import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model using joblib
loaded_model = joblib.load('svmmodel.pkl')

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
st.title('Epilepsy Prediction App')

st.write('Welcome to the Epilepsy Prediction App! Enter patient information and upload a CSV file for prediction.')
# Centered image
st.image("eeg.png",width=500)


# Sidebar for input fields
st.sidebar.header('Patient Information')
patient_name = st.sidebar.text_input('Patient Name')
patient_age = st.sidebar.number_input('Patient Age', min_value=1, max_value=100, value=30)
patient_gender = st.sidebar.selectbox('Patient Gender', ['Male', 'Female', 'Other'])

# Upload CSV file
st.sidebar.header('Upload CSV File')
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Preprocessing using StandardScaler
sc = StandardScaler()

# Main content area

col1, col2 = st.columns(2)


# Display patient information
with col1:
    st.header('Patient Information')
    st.write(f'**Name:** {patient_name}')
    st.write(f'**Age:** {patient_age} years')
    st.write(f'**Gender:** {patient_gender}')

# Display predictions
with col2:
    st.header('Predictions')
    
    if uploaded_file is not None:
        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the uploaded data
        st.subheader('Uploaded Data:')
        st.write(df)
        
        
        # Preprocess the data
        X_input = df.values  # Assuming all columns are input features
        X_input = sc.fit_transform(X_input)
        
        # Make predictions
        predictions = predict_epilepsy(X_input)
        
        # Display predictions
        st.subheader('Epilepsy Predictions:')
        if predictions[0] == 1:
            st.error("You have symptoms to suffer from Epilepsy.🧠")
           
            st.write("Please approach a doctor for further screening and diagnosis.")
            st.image("result.png")
            show_prevention_measures = st.checkbox("Show Prevention Measures")
            if show_prevention_measures:
                st.subheader("Prevention Measures:")
                st.write("1. Get enough sleep and maintain a regular sleep schedule.")
                st.write("2. Manage stress through relaxation techniques.")
                st.write("3. Avoid excessive alcohol consumption.")
                st.write("4. Follow a balanced diet and stay hydrated.")
                st.write("5. Taking medication as prescribed.")
                st.write("6. Wearing a medical alert bracelet.")
                st.write("7. Avoiding seizure triggers.")
        else:
            st.balloons()
            st.success("You are safe and have no symptoms of Epilepsy, but take care of your health.")
            st.image("healthy.jpg",width=300)
# Add custom styling, images, and icons
st.markdown(
    """
    <style>
    /* Custom CSS styles */
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
    }

    .stApp {
        max-width: 100%;
    }

    .stFrame {
        padding: 20px;
        background-color: #ffffff;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }

    .stHeader {
        background-color: #0074e4;
        color: #fff;
        padding: 10px;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }

    .stTitle {
        font-size: 24px;
        font-weight: bold;
    }

    .stImage {
        max-width: 100%;
        border-radius: 10px;
    }

    .stSidebar {
        background-color: #333;
        color: #fff;
        padding: 20px;
        border-radius: 10px;
    }

    .stWidget {
        background-color: #fff;
        padding: 20px;
        border-radius: 10px;
    }

    .stButton {
        background-color: #0074e4;
        color: #fff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .stButton:hover {
        background-color: #0058a1;
    }

    .stSuccess {
        color: #00a400;
    }

    .stError {
        color: #ff0000;
    }

    .stCheckbox {
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)



st.sidebar.image("epilepsy.jpg", width=300)
st.sidebar.markdown("Epilepsy Prediction and Screening Using EEG")

# Footer
st.sidebar.write("DATA DYNAMOS - 2023")

