# Text-Embedding-Using-Sentence-Transformers

## Project Overview

This project demonstrates how text sentences can be converted into numerical vector representations using the **Sentence Transformers** library.

The project uses the `all-MiniLM-L6-v2` pre-trained model to generate embeddings for different sentences. These numerical embeddings can be used in applications such as semantic search, document similarity, recommendation systems, and Retrieval-Augmented Generation (RAG).

## Objectives

* Load a pre-trained sentence embedding model.
* Convert text sentences into numerical vectors.
* Display the generated embeddings.
* Identify the dimensionality of each embedding.
* Understand how text can be represented mathematically for AI applications.

## Technologies Used

* Python
* Sentence Transformers
* PyTorch
* Scikit-learn
* `all-MiniLM-L6-v2` Model

## Project Structure

```text
Rag_System/
│
└── rag.py
```

## Installation

Open the VS Code terminal and install Sentence Transformers:

```bash
pip install sentence-transformers
```

## How to Run

Navigate to the project folder:

```bash
cd Desktop\Rag_System
```

Run the Python program:

```bash
python rag.py
```

## Program Workflow

The program follows these steps:

1. Import the `SentenceTransformer` library.
2. Load the `all-MiniLM-L6-v2` embedding model.
3. Define a list of input sentences.
4. Convert the sentences into numerical embeddings.
5. Display each sentence and its embedding.
6. Display the number of dimensions in each embedding.

## Input Sentences

The project uses the following sample sentences:

```text
I like playing cricket.
I enjoy playing football.
I am learning data science.
Artificial intelligence is useful.
I love creating new applications.
```

## Embeddings

An embedding is a numerical representation of text.

For example:

```text
Sentence → Embedding Model → Numerical Vector
```

The `all-MiniLM-L6-v2` model converts each sentence into a **384-dimensional vector**.

These vectors allow AI systems to process and compare the meaning of text mathematically.

## Expected Output

The program displays:

```text
Embedding model loaded successfully.

Sentence: I like playing cricket.

Numerical Embedding:
[ ... numerical values ... ]

Number of dimensions: 384
```

The same process is performed for all input sentences.

At the end, the program displays:

```text
Text has been successfully converted into numerical vectors.
```

## Applications

Text embeddings are commonly used in:

* Semantic Search
* Document Similarity
* Recommendation Systems
* Question Answering
* Chatbots
* Retrieval-Augmented Generation (RAG)
* Text Classification
* Information Retrieval

## Conclusion

This project provides a simple introduction to **text embeddings using Sentence Transformers**. It demonstrates how human-readable sentences can be transformed into numerical vectors that can be processed by machine learning and artificial intelligence systems.

## Author

Yuvashri H
