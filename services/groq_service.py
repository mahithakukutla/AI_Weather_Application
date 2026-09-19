from groq import Groq

from config.config import Config


def get_weather_advice(weather):
    if not Config.GROQ_API_KEY:
        return _fallback(weather)
    try:
        client = Groq(api_key=Config.GROQ_API_KEY)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": f"In under 25 words, give a practical tip for {weather['temperature']}°C and {weather['description']}."}],
            max_tokens=60,
        )
        return completion.choices[0].message.content.strip()
    except Exception:
        return _fallback(weather)


def _fallback(weather):
    if weather["temperature"] >= 30:
        return "Stay hydrated, wear sunscreen, and seek shade during the hottest hours."
    if "rain" in weather["description"].lower():
        return "Take an umbrella and allow extra time for wet roads."
    if weather["temperature"] <= 12:
        return "Wear warm layers before heading outdoors."
    return "Light layers should keep you comfortable today."