from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI

class TicketState(dict):
    ticket_text=str
    classification=str
    response=str
    review=str

llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

def classify_agent(state:TicketState):
    text=state["ticket_text"]
    prompt=f"""Classify this customer support ticket into
    -billing
    -technical
    -General
    Ticket:{text}
    Return only the category name"""

    classification=llm.invoke(prompt).content
    state["classification"]=classification.strip()
    return state

def respond_agent(state:TicketState):
    text=state["ticket_state"]
    category=state["classification"]
    prompt = f"""
    You are a helpful customer support assistant.
    The ticket category is {category}.
    Write a clear, polite, and concise response to this user:
    "{text}"
    """
    response=llm.invoke(prompt).content
    state["response"]=response.strip()
    return state

def review_agent(state: TicketState):
    resp = state["response"]
    prompt = f"""
    You are a senior QA reviewer. Check this reply for:
    - Politeness
    - Clarity
    - Usefulness

    Suggest improvements briefly if needed:
    {resp}
    """
    review = llm.invoke(prompt).content
    state["review"] = review.strip()
    return state

def build_graph():
    graph=StateGraph(TicketState)
    graph.add_node("classify",classify_agent)
    graph.add_node("respond",respond_agent)
    graph.add_node("review",review_agent)

    graph.set_entry_point("classify")
    graph.add_edge("classify","review")
    graph.add_edge("review","respond")
    graph.add_edge("respond",END)
    return graph.compile()


def run_agent_pipeline(ticket_text: str):
    graph = build_graph()
    result = graph.invoke({
        "ticket_text": ticket_text,
        "classification": "",
        "response": "",
        "review": ""
    })
    return result









    

