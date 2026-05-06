def save_output(
    question,
    answer
):

    with open(
        "outputs/sample_output.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"Question: {question}\n"
        )

        file.write(
            f"Answer: {answer}\n"
        )

        file.write(
            "-" * 50 + "\n"
        )