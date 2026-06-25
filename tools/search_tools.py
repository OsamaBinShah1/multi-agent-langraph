from langchain.tools import tool

@tool
def word_counter(text: str) -> str:
    """Count the number of words in a piece of text."""
    return f"The text contains {len(text.split())} words."

@tool
def calculate(expression: str) -> str:
    """Safely evaluate a simple mathematical expression."""
    allowed = set("0123456789+-*/()., ")
    if not all(c in allowed for c in expression):
        return "Error: invalid characters."
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"
