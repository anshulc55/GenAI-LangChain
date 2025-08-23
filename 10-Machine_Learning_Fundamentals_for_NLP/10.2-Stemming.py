# NLTK Library - Stemming

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import nltk

# Sample text
text = "Running ran runs easily and quickly."

# Tokenization of Corpus
tokenize_words = word_tokenize(text)
print(f"\nTokenize Words : {tokenize_words}")

# Apply Stemming - Porter Stemmer
porterStemmer = PorterStemmer()
porter_stemmed = [porterStemmer.stem(word) for word in tokenize_words]
print(f"\nPorter Stemmed Words : {porter_stemmed}")

# Apply Stemming - Lanchaster Stemmer
lancasterStemmer = LancasterStemmer()
lancaster_stemmed = [lancasterStemmer.stem(word) for word in tokenize_words]
print(f"\nLanchaster Stemmed Words : {lancaster_stemmed}")
