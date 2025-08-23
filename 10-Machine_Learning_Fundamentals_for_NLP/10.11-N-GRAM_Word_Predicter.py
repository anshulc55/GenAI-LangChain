from collections import defaultdict, Counter
import random

# Sample dataset
corpus = [
    "I love programming in Python",
    "Python programming is fun",
    "I love coding and programming",
    "Machine learning and Python go hand in hand",
    "Programming in Python is rewarding",
    "I also love programming in Go",
]

# Generate N-Grams from a given text.
def generate_n_grams(text, n):
    words = text.lower().split()
    n_grams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    return n_grams

# Train an N-Gram model from a corpus of text.
def train_ngram_model(corpus, n):
    model = defaultdict(Counter)
    for sentence in corpus:
        n_grams = generate_n_grams(sentence, n)
        for n_gram in n_grams:
            prefix, next_word = n_gram[:-1], n_gram[-1]
            model[prefix][next_word] += 1
    return model

# Predict the next word(s) based on the given prefix.
def predict_next_word(model, prefix, n_predictions=3):
    predictions = model.get(prefix, {})
    if predictions:
        sorted_predictions = sorted(predictions.items(), key=lambda x: x[1], reverse=True)
        return [word for word, _ in sorted_predictions[:n_predictions]]
    else:
        # Fallback: Return most common words from the model
        fallback_words = Counter(word for key in model for word in model[key])
        return [word for word, _ in fallback_words.most_common(n_predictions)]

# Step 1: Train a Bigram Model (N=3)
n = 3
n_gram_model = train_ngram_model(corpus, n)

# Step 2: Make Predictions
prefix = ("i", "love")  # User's input (converted to lowercase)
predictions = predict_next_word(n_gram_model, prefix)

# Step 3: Display Predictions
print(f"Input: {' '.join(prefix)}")
print("Predicted next words:", predictions)

# Example usage with random prefixes
random_prefix = random.choice(list(n_gram_model.keys()))
random_predictions = predict_next_word(n_gram_model, random_prefix)
print(f"\nRandom Prefix: {' '.join(random_prefix)}")
print("Predicted next words:", random_predictions)