from tensorflow.keras.models import load_model
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Explicitly specify compile=False
model = load_model("footfall_rnn.h5", compile=False)

# Compile again with the correct loss function
model.compile(optimizer="adam", loss="mse")

# Load scaler and Encoders
def load_pickle_file(filepath):
    try:
        with open(filepath, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {filepath}")
        return None
    
scaler = load_pickle_file("scaler.pkl")


# Function to preprocess input data
def preprocess_data(data):
    data_scaled = scaler.transform(data)
    SEQ_LENGTH = 10
    X = []
    for i in range(len(data_scaled) - SEQ_LENGTH):
        X.append(data_scaled[i:i+SEQ_LENGTH])
    return np.array(X)


# Function to predict future footfall
def predict_future(model, last_sequence, days_to_predict):
    predictions = []
    current_seq = last_sequence
    for _ in range(days_to_predict):
        next_day_pred = model.predict(current_seq.reshape(1, 10, 1))
        predictions.append(next_day_pred[0, 0])
        current_seq = np.append(current_seq[1:], [[next_day_pred[0, 0]]], axis=0)
    return np.array(predictions)


# Streamlit UI
st.title("📊 Restaurant Footfall Prediction with RNN")
st.write("Upload historical footfall data to predict future visitor trends.")


uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file, parse_dates=["Date"], index_col="Date")
    st.write("📅 Uploaded Data Preview:")
    st.write(data.head())

    # Process input data
    X_test = preprocess_data(data)
    last_seq = X_test[-1]  # Last sequence for future prediction

    # Predict next 10 days
    future_predictions = predict_future(model, last_seq, 10)
    future_predictions_actual = scaler.inverse_transform(future_predictions.reshape(-1, 1))

    # Show results
    st.subheader("📉 Future Predictions (Next 10 Days)")
    future_dates = pd.date_range(start=data.index[-1], periods=11, freq='D')[1:]
    predictions_df = pd.DataFrame({"Date": future_dates, "Predicted Footfall": future_predictions_actual.flatten()})
    st.write(predictions_df)

    # Plot predictions
    st.line_chart(predictions_df.set_index("Date"))
