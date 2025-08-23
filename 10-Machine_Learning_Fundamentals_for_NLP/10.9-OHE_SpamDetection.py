# Classify Sentences into Categories (Spam Detection)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Data Preprocessing: Collect sample sentences and labels.
documents = [
    "Get rich quick with this investment.",
    "Important message about your account.",
    "Your free coupon is waiting!",
    "Hey, are you coming to the meeting?",
    "Congratulations, you’ve won a lottery!",
    "Please find attached the project report."
]

# Labels: 1 for Spam, 0 for Not Spam
labels = [1, 0, 1, 0, 1, 0]

# 2. One-Hot Encoding: Convert text data into numerical form using One-Hot Encoding.

# Initialize the One-Hot Encoder (CountVectorizer)
vectorizer = CountVectorizer(binary=True)  # binary=True for one-hot encoding
X = vectorizer.fit_transform(documents)

# Show the vocabulary
print("\n Vocabulary",vectorizer.get_feature_names_out())

# Show the one-hot encoded feature matrix
print("\n One-hot encoded matrix:")
print(X.toarray())

# 3. Model Training: Use a simple machine learning model to classify sentences.

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier (works well for text classification)
classifier = MultinomialNB()
classifier.fit(X_train,y_train)

# Predict the labels on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracyScore = accuracy_score(y_test,y_pred)
print("\n Accuracy:", accuracyScore)


# 4. Prediction: Test the trained model on new sentences.

# New sentences to classify
new_sentences = [
    "Free cash prize waiting for you.",
    "Let's discuss the project details tomorrow."
]

# One-hot encode the new sentences
new_data = vectorizer.transform(new_sentences)

# Predict the categories
predictData = classifier.predict(new_data)

# Output the predicted categories
for sentence, prediction in zip(new_sentences, predictData) :
    label = "Spam" if prediction == 1 else "Not Spam"
    print(f"Sentence: '{sentence}' --> Predicted: {label}") 
