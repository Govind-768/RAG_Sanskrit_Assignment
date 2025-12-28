# preprocess.py

def read_file(path):
    f = open(path, "r", encoding="utf-8")
    data = f.read()
    f.close()
    return data

def remove_extra_lines(text):
    lines = text.split("\n")
    new_lines = []

    for l in lines:
        l = l.strip()
        if l != "":
            new_lines.append(l)
    
    return "\n".join(new_lines)


def split_into_parts(text, limit=500):
    parts = []
    temp = ""

    for line in text.split("\n"):
        if len(temp) + len(line) < limit:
            temp = temp + " " + line
        else:
            parts.append(temp.strip())
            temp = line
    
    if temp != "":
        parts.append(temp.strip())

    return parts

if __name__ == "__main__":
    file_name = "E:\RAG_Sanskrit_GovindSingh\data\Rag_docs.txt"

    original_text = read_file(file_name)
    cleaned_text = remove_extra_lines(original_text)
    text_parts = split_into_parts(cleaned_text)

    print("Total parts created:", len(text_parts))
    print("\nFirst part:\n")
    print(text_parts[0])