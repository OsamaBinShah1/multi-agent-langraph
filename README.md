# 🕸️ Multi-Agent Research System with LangGraph

A production-ready **multi-agent orchestration system** built with LangGraph. Agents collaborate autonomously to research topics, generate content, and review quality.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-green?style=flat-square)

## Agent Graph
```
[START] → [Researcher] → [Writer] → [Reviewer]
                                         ↓ score < 7        ↓ score ≥ 7
                                      [Writer]             [END]
                                    (rewrite loop)
```

## Quick Start
```bash
git clone https://github.com/OsamaBinShah1/multi-agent-langraph.git
cd multi-agent-langraph
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python main.py
```

## Usage
```python
from graph.workflow import run_research_pipeline
result = run_research_pipeline(topic="Latest advances in RAG for enterprise AI")
print(result["final_output"])
```

## Stack
- **LangGraph** — stateful multi-agent orchestration
- **LangChain** — agent frameworks & tool integration
- **OpenAI GPT-4** — LLM backbone

## Author
**Muhammad Osama Bin Shah** — AI Engineer, Frankfurt, Germany
[LinkedIn](https://www.linkedin.com/in/muhammad-osama-bin-shah/)
