# Sanskrit RAG Question Answering System

## Overview

This project implements a lightweight Retrieval-Augmented Generation (RAG) based Question Answering system using Sanskrit documents as the primary knowledge source.

The system retrieves relevant contextual information from Sanskrit text documents and answers user queries in English using transformer-based NLP models. The complete pipeline is designed to run efficiently on CPU without requiring GPU acceleration.

The project demonstrates the practical workflow of document preprocessing, information retrieval, contextual understanding, and question answering using modern Natural Language Processing techniques.

---

## Features

- Sanskrit document preprocessing
- Text chunking pipeline
- Retrieval-Augmented Question Answering
- English query support
- Context-based answer generation
- Lightweight CPU-only implementation
- Modular NLP project structure
- Automatic output saving
- Transformer-based QA pipeline
- TF-IDF based semantic retrieval

---

## Technologies Used

- Python
- Scikit-learn
- HuggingFace Transformers
- PyTorch
- NumPy

---

## Project Structure

```text
RAG_Sanskrit_Assignment/
│
├── data/
│   └── Rag_docs.txt
│
├── outputs/
│   └── sample_output.txt
│
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   ├── retrieve.py
│   ├── generate.py
│   └── utils.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

1. Load Sanskrit documents
2. Clean and preprocess text
3. Split text into smaller chunks
4. Retrieve relevant chunks using TF-IDF similarity
5. Generate contextual answers using a transformer QA model
6. Save outputs automatically

---

## Model Used

### Retrieval
- TF-IDF Vectorizer
- Cosine Similarity

### Question Answering
- DistilBERT Question Answering Pipeline
- Model:
  `distilbert-base-cased-distilled-squad`

---

## Example Queries

```text
Who was in King Bhoj's court?
```

```text
What is the moral of the story?
```

```text
Who was Ghantakarna?
```

---

## Sample Output

```text
Question:
Who was in King Bhoj's court?

Answer:
poet kAlIdAsa
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Govind-768/RAG_Sanskrit_Assignment.git
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Future Improvements

- Add multilingual query support
- Use sentence embeddings for semantic retrieval
- Integrate vector databases like FAISS
- Add Streamlit web interface
- Improve Sanskrit-specific NLP processing
- Add conversational memory support

---

## Learnings

This project helped in understanding:

- Retrieval-Augmented Generation workflows
- Transformer-based Question Answering
- Text preprocessing techniques
- Information retrieval systems
- NLP pipeline design
- Context-aware answer generation
- CPU-efficient transformer deployment

---

## Conclusion

This project demonstrates a lightweight and practical implementation of a Retrieval-Augmented Question Answering system using Sanskrit documents. It combines retrieval techniques with transformer-based NLP models to provide contextual answers for English queries while maintaining a CPU-friendly architecture.

---

## Author

Govind Singh