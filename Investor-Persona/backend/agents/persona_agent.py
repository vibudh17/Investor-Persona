import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def classify_persona(investor_data):

    prompt = f"""
Classify this investor as:

Conservative
Moderate
Aggressive

Investor:
{investor_data}

Answer ONLY one word.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "phi",
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    data = response.json()

    print("OLLAMA RESPONSE:", data)

    result = data.get("response", "").lower()

    if "conservative" in result:
        return "Conservative"
    elif "aggressive" in result:
        return "Aggressive"
    else:
        return "Moderate"