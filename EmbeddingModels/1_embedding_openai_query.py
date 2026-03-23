from langchain_openai import OpenAiEmbeddings
from dotenv import load_dotenv


model = OpenAiEmbeddings(model='text-embedding-3-large', dimensions=32)
vector = model.embed_query("Delhi is the capital of India")

print(str(vector))