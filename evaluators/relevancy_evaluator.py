from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def calculate_relevancy(expected, actual):

    embeddings = model.encode([
        expected,
        actual
    ])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity