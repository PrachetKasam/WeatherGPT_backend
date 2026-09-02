import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.providers.mock_llm import MockLLMProvider, SUPPORTED_LANGUAGES
from app.schemas import (
    AlertsResponse,
    ChatRequest,
    ChatResponse,
    ForecastResponse,
    WeatherResponse,
)
from app.services.chat_service import generate_chat_response
from app.services.weather_service import (
    LocationNotFoundError,
    get_forecast,
    get_weather,
)
from app.data import ALERT_DATA


app = FastAPI(
    title="WeatherGPT Backend",
    description="Backend for WeatherGPT weather, forecast, alert and chat services.",
    version="1.0.0",
)

cors_origins = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
    if origin.strip()
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mock_llm_provider = MockLLMProvider()


@app.get("/")
def home():
    return {"message": "WeatherGPT backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/api/weather", response_model=WeatherResponse)
def weather(city: str):
    try:
        return get_weather(city)
    except LocationNotFoundError:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "LOCATION_NOT_FOUND",
                    "message": f"Weather data not found for {city}.",
                }
            },
        )


@app.get("/api/forecast", response_model=ForecastResponse)
def forecast(city: str):
    try:
        return {"city": city, "forecast": get_forecast(city)}
    except LocationNotFoundError:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "LOCATION_NOT_FOUND",
                    "message": f"Forecast data not found for {city}.",
                }
            },
        )


@app.get("/api/alerts", response_model=AlertsResponse)
def alerts(city: str):
    return {"city": city, "alerts": ALERT_DATA.get(city, [])}


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    if request.language not in SUPPORTED_LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail={
                "error": {
                    "code": "UNSUPPORTED_LANGUAGE",
                    "message": (
                        f"Language '{request.language}' is not supported. "
                        f"Use one of: {', '.join(SUPPORTED_LANGUAGES)}."
                    ),
                }
            },
        )

    try:
        return generate_chat_response(request, mock_llm_provider)
    except LocationNotFoundError:
        raise HTTPException(
            status_code=404,
            detail={
                "error": {
                    "code": "LOCATION_NOT_FOUND",
                    "message": f"Weather data not found for {request.location.city}.",
                }
            },
        )
