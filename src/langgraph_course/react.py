import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_ollama import ChatOllama

load_dotenv()

from azure.identity import DefaultAzureCredential, get_bearer_token_provider
token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    os.getenv("AZURE_TOKEN_PROVIDER")
)

@tool
def triple(num: float) -> float:
    """
    parameter:
        num: float
    return:
        float
    """
    return num * 3

tools = [triple, TavilySearch(max_results=1)]

# llm = ChatOpenAI(
#     base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_key=token_provider,
#     model="gpt-5-nano",
#     temperature=0,
# ).bind_tools(tools)

llm = ChatOllama(
    model="qwen3.8:27b-mlx",
    # temperature=0,
).bind_tools(tools)

