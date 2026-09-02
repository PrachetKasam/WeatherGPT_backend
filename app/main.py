from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.data import WEATHER_DATA, FORECAST_DATA, ALERT_DATA
from app.schemas import (
    WeatherResponse,
    ForecastResponse,
    AlertsResponse
)


# -----------------------------------
# Create the FastAPI application
# -----------------------------------

app = FastAPI(
    title="WeatherGPT Backend",
    description="Backend for WeatherGPT weather, forecast and alert services.",
    version="1.0.0"
)


# -----------------------------------
# CORS
# -----------------------------------
# This allows our future React frontend,
# running on localhost:5173, to communicate
# with this backend.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------------
# Home route
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "WeatherGPT backend is running"
    }


# -----------------------------------
# Health check
# -----------------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -----------------------------------
# Current Weather API
# -----------------------------------

@app.get("/api/weather", response_model=WeatherResponse)
def get_weather(city: str):

    # Check if the city exists in our mock data
    if city not in WEATHER_DATA:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "LOCATION_NOT_FOUND",
                    "message": f"Weather data not found for {city}."
                }
            }
        )

    return WEATHER_DATA[city]


# -----------------------------------
# Forecast API
# -----------------------------------

@app.get("/api/forecast", response_model=ForecastResponse)
def get_forecast(city: str):

    # Check if the city exists
    if city not in FORECAST_DATA:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "LOCATION_NOT_FOUND",
                    "message": f"Forecast data not found for {city}."
                }
            }
        )

    return {
        "city": city,
        "forecast": FORECAST_DATA[city]
    }


# -----------------------------------
# Weather Alerts API
# -----------------------------------

@app.get("/api/alerts", response_model=AlertsResponse)
def get_alerts(city: str):

    # If there are no alerts for the city,
    # return an empty list.
    if city not in ALERT_DATA:
        return {
            "city": city,
            "alerts": []
        }

    return {
        "city": city,
        "alerts": ALERT_DATA[city]
    }


# -----------------------------------
# Temporary Chat API
# -----------------------------------
# This is only a placeholder for now.
# Your teammate will build the real
# chatbot and LLM functionality later.

@app.post("/api/chat")
def chat():

    return {
        "message": "Chat service will be implemented by the AI teammate.",
        "location": "Raipur",
        "language": "en",
        "weather_context": {
            "temperature": 28,
            "condition": "Cloudy",
            "rain_probability": 60
        },
        "sources": [
            "mock_weather"
        ]
    }
    