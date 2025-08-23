# Find News Article Title using TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Sample news articles
news_articles = [
    "The latest iPhone was launched yesterday. It includes several new features in the camera and battery life.",
    "The local football team won their match yesterday, scoring a last-minute goal.",
    "The government has announced new policies aimed at improving the economy and reducing unemployment.",
    "Scientists discovered a new species of bird in the Amazon rainforest, which is attracting a lot of attention.",
    "The basketball championship final was held last night, with Team A beating Team B in a thrilling game.",
    "A new artificial intelligence model can now create realistic images from text prompts, revolutionizing the tech world."
]

# Step 1: Apply TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5)
tfidf_matrix = vectorizer.fit_transform(news_articles)

# Step 2: Extract the most important terms for each article
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray()

# Display important terms for each article
for i, article in enumerate(news_articles):
    print(f"Article {i + 1}: {article}")
    print("Top terms:")
    sorted_indices = np.argsort(-tfidf_scores[i])  # Sort terms by their scores
    for idx in sorted_indices[:3]:  # Top 5 terms
        print(f"  {feature_names[idx]}: {tfidf_scores[i][idx]:.4f}")
    print("\n")
