from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = ["Hugging Face is great", "I love embeddings"]
embeddings = model.encode(sentences)

print(embeddings.shape)  # (2, 384)