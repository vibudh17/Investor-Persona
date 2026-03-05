# Stock Investor Backend

## Overview

This is a FastAPI-based service that analyzes financial news and provides personalized investment recommendations based on an investor's risk profile.

The system uses a multi-agent AI architecture where different agents handle classification, reasoning, and explanation tasks.

The backend integrates with a **local LLM runtime (Ollama)** to generate AI-driven explanations.


# Architecture

The backend follows a **multi-agent design pattern**:


Client (React UI)
        │
        ▼
     FastAPI
        │
        ▼
  Orchestrator Agent
     │        │        │
     ▼        ▼        ▼
Persona   News Logic   Conversation
Agent     (Rules/ML)      Agent
     │                    │
     ▼                    ▼
      Local LLM via Ollama
```

### Agents

**Persona Agent**

* Classifies the investor profile
* Outputs:

  * Conservative
  * Moderate
  * Aggressive

**News Analyzer**

* Matches news sentiment with investor type
* Generates investment recommendation

**Conversation Agent**

* Uses LLM to explain recommendations 
* Generates text explanation
* Optional text-to-speech output

---

# Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| FastAPI    | Backend API framework         |
| Python     | Core language                 |
| Ollama     | Local LLM runtime             |
| Phi Model  | Lightweight LLM for reasoning |
| Requests   | API communication             |

---

# Project Structure

```
backend
│
├── agents
│   ├── persona_agent.py
│   ├── conversation_agent.py
│   └── orchestrator.py
│
├── data
│   └── investors.json
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Create Virtual Environment

```
python -m venv venv
```

Activate:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama.

Then pull the lightweight model:

```
ollama pull phi
```

Test:

```
ollama run phi
```

---

# Running the Backend

Start the API server:

```
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

```
GET /
```

Response

```
{
 "message": "Investor AI Backend Running"
}
```

---

## Get Investor Persona

```
GET /persona/{investor_id}
```

Example

```
GET /persona/1
```

Response

```
{
 "persona": "Conservative"
}
```

---

## Analyze News

```
POST /analyze
```

Request

```
{
 "investor_id": 1,
 "news": "Gold prices increase due to inflation"
}
```

Example Response

```
{
 "persona": "Conservative",
 "recommendation": "Invest",
 "explanation": "Gold often performs well during inflation because investors move money into safe assets."
}
```

