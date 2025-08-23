# NLTK Library - NER

from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
import nltk

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Sample Text
sentence = "Barack Obama was born in Hawaii and was the 44th President of the United States."

# Tokenize the sentence
tokens = word_tokenize(sentence)
print("\nTokens:", tokens)

# POS Tagging
pos_tags = pos_tag(tokens)
print("\nPOS Tags:", pos_tags)

# Perform NER
try:
    named_entities = ne_chunk(pos_tags)
    print("\nNamed Entities:")
    named_entities.pprint()
except Exception as e:
    print("\nError during Named Entity Recognition:", str(e))
