from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableLambda
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

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)


def analze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the pros of these features.",
            ),
        ]
    )
    return pros_template.invoke(features)


# Define cons analysis step
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human",
                "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )
    return cons_template.format_prompt(features=features)


# Combine pros and cons into a final review
def combine_pros_cons(pros, cons):
    return f"Pros:\n{pros}\n\nCons:\n{cons}"

# Simplif branches with LECL


pros_branch_chain = (RunnableLambda(
    lambda x: analze_pros(x)) | model | StrOutputParser())


cons_branch_chain = (
    RunnableLambda(lambda x: analyze_cons(x)) | model | StrOutputParser()
)

chain = prompt_template | model | StrOutputParser() | RunnableParallel(
    branches={"pros": pros_branch_chain, "cons": cons_branch_chain}) | RunnableLambda(lambda x: print(x) or combine_pros_cons(x["branches"]["pros"], x["branches"]["cons"]))


# Run the chain
result = chain.invoke({"product_name": "iPhone 15 pro max"})

print(result)
