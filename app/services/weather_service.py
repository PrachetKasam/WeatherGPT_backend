from typing import Dict, Any

from app.data import FORECAST_DATA, WEATHER_DATA


class LocationNotFoundError(Exception):
    pass


def get_weather(city: str) -> Dict[str, Any]:
    if city not in WEATHER_DATA:
        raise LocationNotFoundError(city)
    return WEATHER_DATA[city]


def get_forecast(city: str) -> list:
    if city not in FORECAST_DATA:
        raise LocationNotFoundError(city)
    return FORECAST_DATA[city]


def create_chat_weather_context(city: str) -> Dict[str, Any]:
    weather = get_weather(city)
    forecast = get_forecast(city)
    current = weather["current"]
    return {
        "temperature": current["temperature"],
        "condition": current["condition"],
        "rain_probability": forecast[0]["rain_probability"],
    }
