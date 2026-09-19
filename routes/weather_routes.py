from flask import Blueprint, jsonify, render_template, request

from services.groq_service import get_weather_advice
from services.weather_service import get_weather
from utils.validators import validate_city

weather_bp = Blueprint("weather", __name__)


@weather_bp.get("/")
def index():
    return render_template("index.html")


@weather_bp.get("/api/weather")
def weather():
    city, error = validate_city(request.args.get("city", ""))
    if error:
        return jsonify(error=error), 400

    data, error, status = get_weather(city)
    if error:
        return jsonify(error=error), status

    data["advice"] = get_weather_advice(data)
    return jsonify(data)