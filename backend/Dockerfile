# ---------- BASE IMAGE ----------
FROM python:3.10

# ---------- SET WORKDIR ----------
WORKDIR /app

# ---------- COPY PROJECT FILES ----------
COPY . /app

# ---------- INSTALL REQUIRED PACKAGES MANUALLY ----------
RUN pip install fastapi uvicorn pymongo python-dotenv langchain langchain-openai langgraph requests

# ---------- EXPOSE PORT ----------
EXPOSE 8000

# ---------- RUN FASTAPI SERVER ----------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
