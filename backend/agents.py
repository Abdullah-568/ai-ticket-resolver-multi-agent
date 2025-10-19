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
    prompt=f"""
    You are an intelligent support ticket classifier.

    Task:
    Analyze the following customer support ticket and classify it into one of these categories:
    - Billing → issues related to payments, invoices, refunds, subscriptions.
    - Technical → issues with app errors, bugs, connectivity, or system features.
    - General → questions, suggestions, or feedback not related to billing or technical issues.

    Ticket:
    "{text}"

    Output:
    Return only the category name (Billing / Technical / General).
    """

    classification=llm.invoke(prompt).content
    state["classification"]=classification.strip()
    return state

def respond_agent(state:TicketState):
    text=state["ticket_state"]
    category=state["classification"]
    prompt = f"""
    You are a helpful and empathetic AI support representative.

    Category: {category}
    Customer Ticket:
    "{text}"

    Task:
    - Write a polite and natural human-like response.
    - Keep it short (2–3 paragraphs).
    - Offer clear next steps or assurance, depending on the category.
    - Maintain professionalism and friendliness in tone.

    Response:
    """
    response=llm.invoke(prompt).content
    state["response"]=response.strip()
    return state

def review_agent(state: TicketState):
    resp = state["response"]
    prompt = f"""
    You are a senior QA reviewer evaluating customer support replies.

    Evaluate the following response for:
    - Tone: Polite, professional, and empathetic?
    - Clarity: Easy to read and understand?
    - Helpfulness: Provides a clear next step or useful information?

    Provide:
    - A rating (1–10)
    - 2–3 lines of constructive feedback for improvement.

    Response to review:
    {resp}

    Output format:
    Rating: <number>/10
    Feedback: <your comments>
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









    


