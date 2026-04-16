from dotenv import load_dotenv
load_dotenv()
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
import warnings
warnings.filterwarnings("ignore")

@tool
def web_search(query: str)-> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"
llm = ChatGroq(model="llama-3.1-8b-instant")
tools = [web_search]
agent = create_react_agent(model=llm,tools=tools)
def main():
    print("Hello from langchain-agentic-ai!")
    result=agent.invoke({"messages": HumanMessage(content="What is the weather in Tokyo")})
    print(result)
if __name__ == "__main__":

    main()

