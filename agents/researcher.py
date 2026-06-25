from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

SYSTEM = """You are an expert AI researcher. Given a topic, identify key aspects,
summarise important facts, trends, and insights. Use structured markdown format."""

def run_researcher(state: dict) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)
    response = llm.invoke([
        SystemMessage(content=SYSTEM),
        HumanMessage(content=f"Research thoroughly: {state['topic']}"),
    ])
    print(f"[Researcher] ✅ Done ({len(response.content.split())} words)")
    return {**state, "research": response.content, "step": "researched"}
