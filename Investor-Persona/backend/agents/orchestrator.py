import json
from agents.persona_agent import classify_persona
from models.news_model import predict_news
from agents.conversation_agent import generate_explanation



def analyze_news(investor, news_text):

    persona_raw = classify_persona(investor)

    if "Conservative" in persona_raw:
        persona = "conservative"
    elif "Aggressive" in persona_raw:
        persona = "aggressive"
    else:
        persona = "moderate"

    news_category = predict_news(news_text)

    if persona == news_category:
        recommendation = "Recommended"
    else:
        recommendation = "Not Recommended"

    explanation = generate_explanation(
        persona,
        news_text,
        recommendation
    )

    return {
        "persona": persona,
        "news_category": news_category,
        "recommendation": recommendation,
        "explanation": explanation
    }