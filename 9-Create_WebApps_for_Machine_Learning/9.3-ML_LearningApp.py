# import module
import streamlit as st
import pickle
import numpy as np

# Title
st.title("House Price Predictor")

# User Inputs 
area = st.number_input("Enter the area (sq ft): ", 1000, 10000)
rooms = st.slider("Number of rooms: ", 1, 10)

# Load the model
model = pickle.load(open("house_price_model.pkl", "rb"))

# Pridict the Price
if st.button("Predict Price"):
    features = np.array([[area, rooms]])
    prediction = model.predict(features)
    st.subheader(f"Predicted Price: ${prediction[0]:,.2f}")
