from flask import Flask

from config.config import Config
from routes.weather_routes import weather_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(weather_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
