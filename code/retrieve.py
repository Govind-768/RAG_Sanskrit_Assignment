# retrieve.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocess import read_file, remove_extra_lines, split_into_parts

def load_parts():
    text = read_file("E:\RAG_Sanskrit_GovindSingh\data\Rag_docs.txt")
    cleaned = remove_extra_lines(text)
    parts = split_into_parts(cleaned)
    return parts

def get_top_matches(question, parts, top_n=3):
    tfidf = TfidfVectorizer()
    part_vectors = tfidf.fit_transform(parts)
    q_vec = tfidf.transform([question])
    scores = cosine_similarity(q_vec, part_vectors)[0]
    ids = scores.argsort()[-top_n:][::-1]
    result = []

    for i in ids:
        result.append(parts[i])

    return result

if __name__ == "__main__":
    all_parts = load_parts()
    user_question = "घण्टाकर्णः कः आसीत्"
    matches = get_top_matches(user_question, all_parts)

    print("Question:", user_question)
    print("\nTop related text:\n")

    for i, m in enumerate(matches, 1):
        print(f"--- Result {i} ---")
        print(m)
        print()
