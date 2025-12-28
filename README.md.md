##### **Sanskrit Document Retrieval-Augmented Generation(RAG) System**



This project is a simple implementation of a Retrieval-Augmented Generation (RAG) system built using Sanskrit documents. The system retrieves relevant text from Sanskrit documents and generates answers for user queries. The complete pipeline is designed to run only on CPU, as required in the assignment.



##### **Project Overview**



* Sanskrit documents are used as the knowledge source
* Text is preprocessed and divided into smaller chunks
* Relevant chunks are retrieved based on  the user query
* A lightweight language model generates an answer using the retrieved text
* No GPU is used at any stage



##### **Folder Structure**



RAG\_Sanskrit\_GovindSingh/

│

├── code/

│   ├── preprocess.py

│   ├── retrieve.py

│   ├── generate.py

│

├── data/

│   └── Rag\_docs.txt

│

├── report/

│   └── Technical\_Report\_RAG\_Assign.pdf

│

└── README.md



##### **Requirements**



* Python 3.9 or above
* Required Python libraries:

&nbsp;	*Scikit-learn*

	*transformers*

	*torch*



Install dependencies using:

 *pip install scikit-learn transformers torch*



##### <b>How to run the project</b>



Step 1: Preprocess the Sanskrit documents

&nbsp;

&nbsp;*python code/preprocess.py*



Step 2: Run the retrieval module



&nbsp;*python code/retrieve.py*



Step 3: Run the generation module

&nbsp;

*python code/generate.py*



##### <b>Notes</b>



* The project uses a lightweight language model for text generation
* Output quality depends on the retrieved context
* The focus of the project is on understanding the RAG workflow rather than language perfection



##### **Conclusion**



This project demonstrates a basic functional RAG pipeline for Sanskrit documents. It follows the assignment guidelines and provide a clear understanding of preprocessing, retrieval, and generation in a CPU-based setup.

&nbsp;

