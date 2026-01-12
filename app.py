import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Diabetes Prediction App")

st.title("🩺 Diabetes Prediction App")

# Load model
@st.cache_resource
def load_model():
    with open("trained_model.sav", "rb") as file:
        return pickle.load(file)

model = load_model()
st.success("Model loaded successfully ✅")

st.subheader("Enter Patient Details")

# Inputs
pregnancies = st.number_input("Pregnancies", 0, 20, 0)
glucose = st.number_input("Glucose Level", 0, 300, 120)
blood_pressure = st.number_input("Blood Pressure", 0, 200, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

# Predict
if st.button("Predict Diabetes"):
    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High chance of Diabetes")
    else:
        st.success("✅ Low chance of Diabetes")
