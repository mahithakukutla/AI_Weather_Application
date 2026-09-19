import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
    WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
