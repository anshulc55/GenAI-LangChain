import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Load trained model
model = load_model("sentiment_rnn.h5")

# Load IMDb word index
word_index = imdb.get_word_index()
word_index = {k: (v + 3) for k, v in word_index.items()}  # Shift indices
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3
reverse_word_index = {v: k for k, v in word_index.items()}  # Reverse lookup

# Function to preprocess user input text
def preprocess_text(review):
    words = review.lower().split()
    tokenized_review = [word_index.get(word, 2) for word in words]  # Default to <UNK> if word not found
    tokenized_review = [idx if idx < num_words else 2 for idx in tokenized_review]  # Ensure within vocabulary range
    padded_review = pad_sequences([tokenized_review], maxlen=200, padding='post', truncating='post')
    return padded_review

# Streamlit UI
st.title("📝 Sentiment Analysis with RNN")
st.write("Enter a movie review, and our model will predict if it's positive or negative!")

# User input
review_text = st.text_area("Enter a movie review:")

if st.button("Analyze Sentiment"):
    processed_review = preprocess_text(review_text)
    prediction = model.predict(processed_review)[0][0]
    
    # Display result
    if prediction > 0.5:
        st.success(f"✅ Positive Sentiment! (Confidence: {prediction:.2f}) 😊")
    else:
        st.error(f"❌ Negative Sentiment! (Confidence: {1 - prediction:.2f}) 😡")