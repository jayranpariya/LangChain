from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

BASE_URL = os.getenv('OPENAI_BASE_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# Load environment variables from .env
load_dotenv()
# Now you can access your environment variables

# Create a ChatOpenAI model
model = ChatOpenAI(
    base_url=BASE_URL,
    api_key=OPENAI_API_KEY,
    model="gpt-4o-mini",
    temperature=1,
    max_tokens=4096,
    top_p=0.99
)

messages = [

]


# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
