from dotenv import load_dotenv
from graph.workflow import run_research_pipeline
load_dotenv()

result = run_research_pipeline("How RAG works in production AI systems")
print("\n📄 FINAL DRAFT:")
print(result["draft"])
