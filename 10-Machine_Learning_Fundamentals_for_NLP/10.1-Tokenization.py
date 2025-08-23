from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.sentiment import  SentimentIntensityAnalyzer
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download necessary NLTK data
# Ensures required datasets for tokenization, stop-word removal, and sentiment analysis are available
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')

# Raw Review Text
review_text = "The movie was absolutely fantastic! The plot and acting were top-notch."
#review_text = "Apple is banana, banana is fruit."

# Step 1: Tokenization
word_tokens = word_tokenize(review_text)
# print(f"Tokens : {word_tokens}")

# Step 2: Stop Word Removal
stop_words = set(stopwords.words("english"))
# print(f"\nStop Words from English : {stop_words}")

filter_tokens = [word for word in word_tokens if word.lower() not in stop_words and word.isalnum()]
# print("\nFiltered Tokens (after Stop Word Removal):", filter_tokens)

# Step 3: TF-IDF Weighting
# Example corpus with multiple reviews
corpus = [
    "The movie was absolutely fantastic! The plot and acting were top-notch.",
    "The movie was okay, but the acting could have been better.",
    "I did not like the movie. The plot was too slow."
]


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()

tfidf_dict = {feature_names[i]: tfidf_matrix[0, i] for i in range(len(feature_names))}
#print("TF-IDF Weights for the first review:", tfidf_dict)


# Step 4: Sentiment Detection
sAnalyser = SentimentIntensityAnalyzer()
sentiment_scores = sAnalyser.polarity_scores(review_text)
# print("Sentiment Scores:", sentiment_scores)

# Final Sentiment
if sentiment_scores['compound'] > 0:
    sentiment = "Positive"
elif sentiment_scores['compound'] < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Overall Sentiment:", sentiment)





