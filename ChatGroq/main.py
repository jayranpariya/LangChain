from dotenv import load_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
import os

# Load environment variables from .env
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Create a ChatGroq model
model = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192"
)

# Create a simple prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that can answer questions and help with tasks."),
    ("human", "{input}")
])

# Create the chain
chain = prompt | model | StrOutputParser()

try:
    # Invoke the chain with a message
    result = chain.invoke({"input": "Create Lambda Layers ?"})

    print("Result:")
    print(result)
except (ValueError, KeyError, ImportError, AttributeError) as e:
    print(f"An error occurred: {str(e)}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
