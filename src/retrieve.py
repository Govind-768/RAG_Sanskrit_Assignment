from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_context(
    query,
    chunks,
    top_k=3
):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(
        chunks + [query]
    )

    similarity = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    top_indices = similarity[0].argsort()[-top_k:][::-1]

    retrieved_chunks = []

    for idx in top_indices:

        retrieved_chunks.append(
            chunks[idx]
        )

    combined_context = " ".join(
        retrieved_chunks
    )

    return combined_context