# One Hot Encoding

from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Sample Data
tokens = ["cat", "dog", "mouse"]

# Using Scikit-learn for One-Hot Encoding
words = np.array(tokens).reshape(-1,1)
#print(words)

# Initilize the OHE
encoder = OneHotEncoder(sparse_output=False)
one_hot_matrix = encoder.fit_transform(words)
print(one_hot_matrix)

# Transform new data
new_word = np.array(["dog"]).reshape(-1, 1)
encoded_new_word = encoder.transform(new_word)
print(f"One-hot encoding for 'dog': {encoded_new_word}")