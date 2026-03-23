# from groq import Groq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# response = client.chat.completions.create(
#     model="llama-3.1-8b-instant",  # ✅ use this
#     messages=[
#         {"role": "user", "content": "What is the capital of India?"}
#     ]
# )

# print(response.choices[0].message.content)

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

result = model.invoke("What is the capital of India?")

print(result.content)