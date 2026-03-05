from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
from agents.persona_agent import classify_persona
from agents.orchestrator import analyze_news


app = FastAPI()

# Enable CORS
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsRequest(BaseModel):
    investor_id: int
    news: str

@app.get("/")
def home():
    return {"message": "Investor AI Backend Running"}


@app.get("/persona/{investor_id}")
def get_persona(investor_id: int):

    with open("data/investors.json") as f:
        investors = json.load(f)

    investor = next(i for i in investors if i["id"] == investor_id)

    persona = classify_persona(investor)

    return {"persona": persona}

@app.post("/analyze")
def analyze(request: NewsRequest):

    with open("data/investors.json") as f:
        investors = json.load(f)

    investor = next(i for i in investors if i["id"] == request.investor_id)

    result = analyze_news(investor, request.news)

    return result