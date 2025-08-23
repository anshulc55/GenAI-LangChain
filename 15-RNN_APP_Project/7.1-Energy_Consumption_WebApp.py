# Create the Streamlit Web App

import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import pickle

# Load the trained model and scaler
model = load_model("energy_rnn_model.h5", compile=False)
# Compile again with the correct loss function
model.compile(optimizer="adam", loss="mse")

with open("scaler_1.pkl", "rb") as f:
    scaler = pickle.load(f)

# Streamlit App
st.title("🔋 Energy Consumption Prediction")
st.write("This app predicts energy consumption based on past 24 hours of data.")

# Create input fields
st.sidebar.header("Enter last 24 hours data")

input_data = []
for i in range(24):
    col1, col2, col3, col4 = st.sidebar.columns(4)
    energy = col1.number_input(f"Energy[{i+1}]", min_value=0.0, step=0.1)
    temp = col2.number_input(f"Temp[{i+1}]", min_value=-10.0, step=0.1)
    humidity = col3.number_input(f"Humidity[{i+1}]", min_value=0.0, max_value=100.0, step=1.0)
    wind = col4.number_input(f"Wind[{i+1}]", min_value=0.0, step=0.1)
    input_data.append([energy, temp, humidity, wind, i, 15, 6])  # Hour, Day, Month (Example: Day 15, June)

if st.sidebar.button("Predict Energy Consumption"):
    # Convert to NumPy array and reshape
    input_data = np.array(input_data).reshape(1, 24, -1)

    # Make prediction
    prediction = model.predict(input_data)

    # Convert prediction back to original scale
    prediction_rescaled = scaler.inverse_transform(
        np.c_[prediction, np.zeros((len(prediction), input_data.shape[2]-1))]
    )[:, 0]

    # Display result
    st.success(f"⚡ Predicted Energy Consumption: {round(prediction_rescaled[0], 2)} kWh")
