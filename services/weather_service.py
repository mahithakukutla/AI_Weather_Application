import requests

from config.config import Config


def get_weather(city):
    if not Config.OPENWEATHER_API_KEY:
        return None, "OPENWEATHER_API_KEY is not configured.", 500
    try:
        response = requests.get(
            Config.WEATHER_BASE_URL,
            params={"q": city, "appid": Config.OPENWEATHER_API_KEY, "units": "metric"},
            timeout=10,
        )
    except requests.RequestException:
        return None, "Weather service is unavailable.", 503
    if response.status_code == 404:
        return None, "City not found.", 404
    if not response.ok:
        return None, "Unable to retrieve weather data.", 502

    source = response.json()
    return {
        "city": source["name"], "country": source["sys"]["country"],
        "temperature": round(source["main"]["temp"]),
        "feels_like": round(source["main"]["feels_like"]),
        "humidity": source["main"]["humidity"], "wind_speed": source["wind"]["speed"],
        "description": source["weather"][0]["description"].capitalize(),
        "icon": source["weather"][0]["icon"],
    }, None, 200