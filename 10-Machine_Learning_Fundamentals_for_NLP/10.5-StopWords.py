# NLTK Library - Stop Words

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download("stopwords")
nltk.download("punkt")

# Sample Text
sentence = "Green power installation startup SolarSquare raises $40 mn in Series B, led by Lightspeed Venture Partners"

# Tokenize the sentence
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)

# Remove stop words

# Get the English stop words
stop_words = set(stopwords.words('english'))
stop_words.add("$")
stop_words.add(",")
#print("\nEnglish Totel Stop Words : ", stop_words)

tokens_without_stopwords = [word for word in tokens if word.lower() not in stop_words]
print("\nTokens without stop words:", tokens_without_stopwords)
