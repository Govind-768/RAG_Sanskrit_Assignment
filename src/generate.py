from transformers import pipeline


qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad",
    framework="pt"
)


def generate_answer(
    question,
    context
):

    result = qa_pipeline(
        question=question,
        context=context[:1500]
    )

    return result["answer"]