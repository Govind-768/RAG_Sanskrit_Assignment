# generate.py

from transformers import pipeline
from retrieve import load_parts, get_top_matches

def generate_answer(question):
    parts = load_parts()
    context_parts = get_top_matches(question, parts, top_n=2)
    context = " ".join(context_parts)

    prompt = (
        "Answer the question using the given context.\n\n"
        "Context:\n" + context + "\n\n"
        "Question:\n" + question + "\n\n"
        "Answer:"
    )

    generator = pipeline(
    "text-generation",
    model="distilgpt2",
    framework="pt",   
    device=-1 
    )

    output = generator(
        prompt,
        max_length=150,
        do_sample=True,
        temperature=0.7
    )
    return output[0]["generated_text"]

if __name__ == "__main__":
    user_question = "घण्टाकर्णः कः आसीत्"
    answer = generate_answer(user_question)

    print("Question:", user_question)
    print("\nGenerated Answer:\n")
    print(answer)
