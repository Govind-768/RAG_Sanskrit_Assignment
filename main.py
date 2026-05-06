from src.preprocess import (
    load_documents,
    clean_text,
    create_chunks
)

from src.retrieve import (
    retrieve_context
)

from src.generate import (
    generate_answer
)

from src.utils import (
    save_output
)


def main():

    print("Loading documents...")

    text = load_documents(
        "data/Rag_docs.txt"
    )

    print("Cleaning text...")

    cleaned_text = clean_text(text)

    print("Creating chunks...")

    chunks = create_chunks(
        cleaned_text
    )

    question = input(
        "\nEnter your question: "
    )

    print("\nRetrieving context...")

    context = retrieve_context(
    question,
    chunks
    )
    

    print("\nGenerating answer...")

    answer = generate_answer(
        question,
        context
    )

    print("\nAnswer:\n")

    print(answer)

    save_output(
        question,
        answer
    )

    print(
        "\nOutput saved successfully."
    )


if __name__ == "__main__":
    main()