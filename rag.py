from sentence_transformers import SentenceTransformer



model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully.")



sentences = [
    "I like playing cricket.",
    "I enjoy playing football.",
    "I am learning data science.",
    "Artificial intelligence is useful.",
    "I love creating new applications."
]



embeddings = model.encode(sentences)



for i, sentence in enumerate(sentences):

    print("\nSentence:", sentence)

    print("Numerical Embedding:")
    print(embeddings[i])

    print("Number of dimensions:", len(embeddings[i]))


print("\nText has been successfully converted into numerical vectors.")