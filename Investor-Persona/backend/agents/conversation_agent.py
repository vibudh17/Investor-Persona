import requests
from gtts import gTTS

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_explanation(persona, news, recommendation):

    prompt = f"""
    You are a financial advisor.

    Persona: {persona}
    News: {news}
    Recommendation: {recommendation}

    Explain in simple language why this recommendation was given.
    Keep it short.
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

    if "response" in data:
        return data["response"]
    else:
        return "AI explanation unavailable due to memory issue."



def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")