import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi import FastAPI
from dotenv import load_dotenv

from backend.workflows.pipeline import run_pipeline

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/submit-idea")
def submit_idea(idea: str):
    result = run_pipeline(idea)
    return result

@app.get("/")
def root():
    return {"message": "Startup Validator API is running"}


