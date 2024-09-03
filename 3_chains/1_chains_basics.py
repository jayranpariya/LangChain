from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
import os

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

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a comedian who tells jokes about {topic}."),
        ("human", "Tell me {joke_count} jokes."),
    ]
)


chain = prompt_template | model | StrOutputParser()

result = chain.invoke({"topic": "lawyers", "joke_count": 3})

print(result)
