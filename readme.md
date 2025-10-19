🧠 AI Ticket Resolver — LangGraph-Powered Multi-Agent System

An intelligent, end-to-end AI ticket management system built using LangGraph, FastAPI, Streamlit, MongoDB, and Docker.
The project automates customer support by classifying, responding to, and reviewing support tickets using multiple AI agents — all deployed seamlessly on AWS EC2.

🚀 Key Features
🤖 Multi-Agent Workflow (LangGraph)

Implemented using LangGraph, which enables graph-based orchestration of multiple AI agents.

Agents include:

Classifier Agent → categorizes tickets into Billing, Technical, or General.

Responder Agent → generates a polite, context-aware response.

Reviewer Agent → evaluates the quality and tone of the AI’s reply.

Agents are connected via a state graph, ensuring smooth flow of data between stages.

⚡ FastAPI Backend

Acts as the gateway for all AI logic.

Exposes REST APIs to create, process, and retrieve support tickets.

Communicates directly with MongoDB to log tickets and responses.

💾 MongoDB Database

Stores all ticket data, classifications, and AI-generated replies.

Enables tracking of conversation history and model performance.

🖥️ Streamlit Frontend

Interactive UI for viewing and managing tickets.

Sends and retrieves data via FastAPI endpoints.

🐳 Dockerized for Deployment

Each service (backend, frontend, and database) runs inside its own Docker container.


🧠 Learning Outcomes

Practical understanding of LangGraph-based agent orchestration.

Real-world FastAPI–MongoDB integration.

Hands-on experience with Dockerized multi-service deployment on EC2.

Experience building an AI-driven workflow from scratch.



Managed through a single docker-compose.yml file for simplified orchestration.

Easily deployable to AWS EC2 — one command spins up the entire system.
