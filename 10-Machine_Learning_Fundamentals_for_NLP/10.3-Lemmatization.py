# NLTK Library - Lemmatization

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

# Download required resources
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

def lemmatization_fun1():
    # Sample text
    text = "The striped bats are hanging on their feet for best."

    # Tokenize the text
    words = word_tokenize(text)
    print("\nTokenized words:", words)
    print("\n")

    # Apply Lemmatization
    lemmatize = WordNetLemmatizer()
    lemmatize_words = [lemmatize.lemmatize(word, pos=wordnet.VERB) for word in words]
    print("\nLemmatized words:", lemmatize_words)

def lemmatization_fun2():
    # A sentiment analysis system needs to normalize customer reviews for consistent analysis.
    reviews = ["The cats were running around.", "A better solution was provided."]
    lemmatized_reviews = []
    lemmatize = WordNetLemmatizer()

    for review in reviews:
        words = word_tokenize(review)
        lemmatize_words = [lemmatize.lemmatize(word, pos=wordnet.VERB) for word in words]
        lemmatized_reviews.append(" ".join(lemmatize_words))

    print("\n Raw Reviews:", reviews)
    print("\n Lemmatized Reviews:", lemmatized_reviews)

lemmatization_fun2()

