from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# Load environment variables from .env
load_dotenv()

# Now you can access your environment variables
BASE_URL = os.getenv('OPENAI_BASE_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

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
    SystemMessage(content="Solve the following math problems."),
    HumanMessage(content="What is 81 divided by 9?")
]


# Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")

# AIMessage:
#   Message from an AI model.

messages = [
    SystemMessage(content="Solve the following math problems."),
    HumanMessage(content="What is 81 divided by 9?"),
    AIMessage(content="81 divided by 9 is 9."),
    HumanMessage(content="What is 10 times 5?"),
]


# Invoke the model with a message
result = model.invoke(messages)
print(f"Answer from AI: {result.content}")
