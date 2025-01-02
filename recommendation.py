from sqlalchemy.orm import Session
from models import Product
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_products(query: str, db: Session):
    products = db.query(Product).all()
    product_descriptions = [p.name + " " + p.description for p in products]

    # Vectorize using TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(product_descriptions)

    # Add the query
    query_vector = vectorizer.transform([query])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(query_vector, vectors).flatten()
    recommendations = sorted(
        [(products[i], similarity_scores[i]) for i in range(len(products))],
        key=lambda x: x[1],
        reverse=True,
    )

    return [{"name": r[0].name, "score": r[1]} for r in recommendations[:5]]
