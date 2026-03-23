from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
model = HuggingFaceEmbeddings(model_name =  "BAAI/bge-small-en-v1.5")


query = 'tell me about bumrah'

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query_vector = model.embed_query(query)
document_vector = model.embed_documents(documents)

similarity = cosine_similarity([query_vector], document_vector)[0]

index, score =  sorted(list(enumerate(similarity)),key=lambda x:x[1])[-1]

print(documents[index])