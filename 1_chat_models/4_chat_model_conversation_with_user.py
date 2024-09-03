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

chat_history = []  # Create an empty chat history

# Set an initial system message (optional)
system_message = SystemMessage(content="You are a helpful AI assistant.")
chat_history.append(system_message)  # Add system message to chat history


while True:
    query = input("You: ")  # Get user input
    if query.lower() == "exit":
        break
    # Add user message to chat history
    chat_history.append(HumanMessage(content=query))

    # Get AI response using the chat history
    result = model.invoke(chat_history)
    response = result.content
    # Add user message to chat history
    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")  # Print AI response

print("---Messages History---")
print(chat_history)  # Print chat history
