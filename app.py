import streamlit as st
import pickle

st.title("My Machine Learning App")

# Load trained model
model = pickle.load(open("trained_model.sav", "rb"))

st.write("Model loaded successfully ✅")

# Example input
input_value = st.number_input("Enter a value")

if st.button("Predict"):
    prediction = model.predict([[input_value]])
    st.success(f"Prediction: {prediction[0]}")
