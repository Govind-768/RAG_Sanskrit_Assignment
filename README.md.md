# Sanskrit Document Retrieval-Augmented Generation (RAG) System

This project is a simple implementation of a Retrieval-Augmented Generation (RAG) system using Sanskrit documents. The main aim of this project is to retrieve relevant information from Sanskrit text and generate answers for user queries. The complete pipeline is designed to run only on CPU, as mentioned in the assignment.

## Project Overview

- Sanskrit documents are used as the main knowledge source  
- Text is preprocessed and divided into smaller chunks  
- Relevant chunks are retrieved based on the user query  
- A lightweight language model generates answers using the retrieved text  
- No GPU is used at any stage  

## Folder Structure

```
RAG_Sanskrit_Assignment/
├── code/
│   ├── preprocess.py
│   ├── retrieve.py
│   └── generate.py
├── data/
│   └── Rag_docs.txt
├── report/
│   └── Technical_Report_RAG_Assign.pdf
└── README.md
```



## Requirements

- Python 3.9 or above  
- Required Python libraries:
  - scikit-learn  
  - transformers  
  - torch  

Install dependencies using:
pip install scikit-learn transformers torch


## How to Run the Project

Step 1: Preprocess the Sanskrit documents  
python code/preprocess.py


Step 2: Run the retrieval module  
python code/retrieve.py


Step 3: Run the generation module  
python code/generate.py


## Notes

- The project uses a lightweight language model for text generation  
- Output quality depends on the retrieved context  
- Some answers may not be perfect, but they are based on the document content  
- The focus of this project is learning the RAG workflow rather than language perfection  

## Conclusion

This project demonstrates a basic and working RAG pipeline for Sanskrit documents. It follows the assignment guidelines and provides a clear understanding of preprocessing, retrieval, and generation in a CPU-based setup.
