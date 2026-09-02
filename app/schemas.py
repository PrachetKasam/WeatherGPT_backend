from typing import List

from pydantic import BaseModel, Field


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


class ForecastDay(BaseModel):
    date: str
    temperature_high: float
    temperature_low: float
    condition: str
    rain_probability: float


class ForecastResponse(BaseModel):
    city: str
    forecast: List[ForecastDay]


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


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    error: ErrorDetail


class ChatLocation(BaseModel):
    city: str = Field(min_length=1)
    latitude: float
    longitude: float


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    location: ChatLocation
    language: str = Field(min_length=2, max_length=2)


class WeatherContext(BaseModel):
    temperature: float
    condition: str
    rain_probability: float


class ChatResponse(BaseModel):
    message: str
    location: str
    language: str
    weather_context: WeatherContext
    sources: List[str]
