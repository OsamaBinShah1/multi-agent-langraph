import re
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

SYSTEM = """Review the draft. Respond EXACTLY as:
SCORE: <0-10>
FEEDBACK: <detailed feedback>
Be strict — only give 8+ for excellent work."""

def run_reviewer(state: dict) -> dict:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke([
        SystemMessage(content=SYSTEM),
        HumanMessage(content=f"Topic: {state['topic']}\n\nDraft:\n{state['draft']}"),
    ])
    text = response.content
    score = float(re.search(r"SCORE:\s*(\d+(?:\.\d+)?)", text).group(1)) if re.search(r"SCORE:\s*(\d+(?:\.\d+)?)", text) else 5.0
    feedback_m = re.search(r"FEEDBACK:\s*(.+)", text, re.DOTALL)
    feedback = feedback_m.group(1).strip() if feedback_m else text
    passed = score >= 7.0
    print(f"[Reviewer] Score: {score}/10 — {'✅ PASSED' if passed else '🔄 REWRITE'}")
    return {**state, "score": score, "feedback": feedback, "passed": passed, "step": "reviewed"}
