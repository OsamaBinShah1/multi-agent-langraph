from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

SYSTEM = """You are an expert technical writer. Given research notes, write a clear,
well-structured markdown article with an introduction, sections, and conclusion."""

def run_writer(state: dict) -> dict:
    feedback = state.get("feedback", "")
    rewrite_count = state.get("rewrite_count", 0)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    prompt = f"Topic: {state['topic']}\n\nResearch:\n{state['research']}"
    if feedback:
        prompt += f"\n\nPrevious feedback to address:\n{feedback}"
    response = llm.invoke([SystemMessage(content=SYSTEM), HumanMessage(content=prompt)])
    print(f"[Writer] ✅ Draft #{rewrite_count + 1} ({len(response.content.split())} words)")
    return {**state, "draft": response.content, "rewrite_count": rewrite_count + 1, "step": "written"}
