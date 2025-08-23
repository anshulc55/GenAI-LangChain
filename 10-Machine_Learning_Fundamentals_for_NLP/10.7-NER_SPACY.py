# SPACY Library - NER

import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Sample Text
sentence = "Barack Obama was born in Hawaii and was the 44th President of the United States."

# Process the Text
processed_text = nlp(sentence)

for ent in processed_text.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")
