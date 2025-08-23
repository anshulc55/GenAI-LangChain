# NLTK Library - POS Tagging

from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')

# Sample Text
sentence = "Green power installation startup SolarSquare raises $40 mn in Series B, led by Lightspeed Venture Partners"

# Tokenize the sentence
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)

# POS Tagging
pos_tags = pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

# Extract nouns from the sentence
nouns = [word for word, tag in pos_tags if tag in ['NN', 'NNP']]
print("\nNouns:", nouns)

