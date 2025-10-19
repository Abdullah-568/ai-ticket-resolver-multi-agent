from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from agents import run_agent_pipeline
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="AI Ticket Manager")


MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URL)
db = client["support_system"]
tickets = db["tickets"]


class Ticket(BaseModel):
    title: str
    description: str


@app.get("/")
def home():
    return {"message": "✅ AI Ticket Manager API is live!"}

@app.post("/tickets/")
def create_ticket(ticket: Ticket):
    """Create a new ticket and process it through AI pipeline."""
    ai_result = run_agent_pipeline(ticket.description)

    doc = {
        "title": ticket.title,
        "description": ticket.description,
        "classification": ai_result["classification"],
        "response": ai_result["response"],
        "review": ai_result["review"]
    }

    tickets.insert_one(doc)
    return {
        "status": "✅ Success",
        "message": "Ticket processed successfully",
        "data": doc
    }

@app.get("/tickets/")
def list_tickets():
    """View all tickets (without MongoDB IDs)."""
    return {"tickets": list(tickets.find({}, {"_id": 0}))}
