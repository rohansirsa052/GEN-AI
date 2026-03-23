from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model_name =  "BAAI/bge-small-en-v1.5")

text = "Delhi is the capital of India"

vector = model.embed_query(text)

print(len(vector))