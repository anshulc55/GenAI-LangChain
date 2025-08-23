# Movie Review Classification (Positive vs. Negative) using the Bag of Words model

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords

# Sample data: movie reviews and their corresponding labels (0 = negative, 1 = positive)
reviews = [
    "The movie was fantastic! I loved it.",
    "Worst movie ever. Complete waste of time.",
    "Amazing film with great acting.",
    "The plot was boring and predictable.",
    "I absolutely loved the storyline. Great characters!",
    "Terrible movie. Wouldn't recommend it to anyone.",
    "What a great movie! So much fun.",
    "Horrible movie. A waste of money.",
    "One of the best movies I've seen in years.",
    "The movie was awful and too long."
]

# Labels (1 = Positive, 0 = Negative)
labels = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# Preprocessing: Removing stopwords
stop_words = stopwords.words("english")

# Tokenize the reviews and remove stopwords
reviews_processed = [' '.join([word for word in review.split() if word.lower() not in stop_words]) for review in reviews]

# Convert text data into Bag of Words (BoW) vectors using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews_processed)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predict the labels on the test data
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

# Print results
print("Accuracy:", accuracy)


# Example of predictions
new_reviews = [
    "I hated the movie. It was terrible.",
    "This film was awesome, definitely a must-watch!"
]

new_reviews_processed = [' '.join([word for word in review.split() if word.lower() not in stop_words]) for review in new_reviews]
new_reviews_vectorized = vectorizer.transform(new_reviews_processed)
new_predictions = classifier.predict(new_reviews_vectorized)

print("\nPredictions for new reviews:")
for review, prediction in zip(new_reviews, new_predictions):
    print(f"Review: {review} - Prediction: {'Positive' if prediction == 1 else 'Negative'}")
