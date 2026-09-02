from pydantic import BaseModel
from typing import List


# -------------------------
# Current Weather
# -------------------------

class Coordinates(BaseModel):
    latitude: float
    longitude: float


class CurrentWeather(BaseModel):
    temperature: float
    feels_like: float
    condition: str
    humidity: float
    wind_speed: float
    wind_direction: str
    uv_index: float


class WeatherResponse(BaseModel):
    city: str
    state: str
    country: str
    coordinates: Coordinates
    current: CurrentWeather
    updated_at: str


# -------------------------
# Forecast
# -------------------------

class ForecastDay(BaseModel):
    date: str
    temperature_high: float
    temperature_low: float
    condition: str
    rain_probability: float


class ForecastResponse(BaseModel):
    city: str
    forecast: List[ForecastDay]


# -------------------------
# Weather Alerts
# -------------------------

class Alert(BaseModel):
    id: str
    severity: str
    title: str
    description: str
    start_time: str
    end_time: str


class AlertsResponse(BaseModel):
    city: str
    alerts: List[Alert]


# -------------------------
# Error Response
# -------------------------

class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    error: ErrorDetail
