from typing import TypedDict, Optional
from langgraph.graph import StateGraph, END
from agents.researcher import run_researcher
from agents.writer import run_writer
from agents.reviewer import run_reviewer

class AgentState(TypedDict):
    topic: str
    research: Optional[str]
    draft: Optional[str]
    score: Optional[float]
    feedback: Optional[str]
    passed: Optional[bool]
    rewrite_count: int
    step: str

def route_after_review(state: AgentState) -> str:
    if state.get("passed") or state.get("rewrite_count", 0) >= 3:
        return "end"
    return "rewrite"

def build_graph():
    g = StateGraph(AgentState)
    g.add_node("researcher", run_researcher)
    g.add_node("writer", run_writer)
    g.add_node("reviewer", run_reviewer)
    g.set_entry_point("researcher")
    g.add_edge("researcher", "writer")
    g.add_edge("writer", "reviewer")
    g.add_conditional_edges("reviewer", route_after_review, {"end": END, "rewrite": "writer"})
    return g.compile()

def run_research_pipeline(topic: str) -> AgentState:
    app = build_graph()
    state = {"topic": topic, "research": None, "draft": None, "score": None,
             "feedback": None, "passed": False, "rewrite_count": 0, "step": "start"}
    print(f"\n🚀 Pipeline: '{topic}'")
    result = app.invoke(state)
    print(f"✅ Done. Score: {result['score']}/10  Rewrites: {result['rewrite_count']}")
    return result
