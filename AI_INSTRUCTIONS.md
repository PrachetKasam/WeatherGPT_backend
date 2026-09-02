# WeatherGPT Backend — AI Development Instructions

We are building the backend for a Smart India Hackathon project.

Project:
WeatherGPT — Conversational AI for Weather Forecasting,
Alerts, and Climate Information.

The frontend is React + Vite + JavaScript.

The backend must NOT be tightly coupled to the frontend.

## Technology

Use:

- Python
- FastAPI
- Pydantic
- Uvicorn

Use REST APIs.

## Backend Base URL

Development:

http://localhost:8000

Swagger:

/docs

OpenAPI:

/openapi.json

## Required API Endpoints

GET /api/weather
GET /api/forecast
GET /api/alerts
POST /api/chat

## Weather Contract

GET /api/weather?city=Raipur

Response:

{
  "city": "Raipur",
  "state": "Chhattisgarh",
  "country": "India",
  "coordinates": {
    "latitude": 21.2514,
    "longitude": 81.6296
  },
  "current": {
    "temperature": 28,
    "feels_like": 30,
    "condition": "Cloudy",
    "humidity": 72,
    "wind_speed": 14,
    "wind_direction": "North East",
    "uv_index": 5
  },
  "updated_at": "2026-09-02T15:30:00+05:30"
}

DO NOT rename fields.

## Forecast Contract

GET /api/forecast?city=Raipur

Response:

{
  "city": "Raipur",
  "forecast": [
    {
      "date": "2026-09-02",
      "temperature_high": 30,
      "temperature_low": 25,
      "condition": "Cloudy",
      "rain_probability": 60
    }
  ]
}

Support at least 7 days.

## Alerts Contract

GET /api/alerts?city=Raipur

Response:

{
  "city": "Raipur",
  "alerts": [
    {
      "id": "alert-001",
      "severity": "warning",
      "title": "Heavy rainfall possible",
      "description": "Heavy rainfall is possible during the evening.",
      "start_time": "2026-09-02T17:00:00+05:30",
      "end_time": "2026-09-03T06:00:00+05:30"
    }
  ]
}

If there are no alerts:

{
  "city": "Raipur",
  "alerts": []
}

## Chat Contract

POST /api/chat

Request:

{
  "message": "Will it rain tomorrow?",
  "location": {
    "city": "Raipur",
    "latitude": 21.2514,
    "longitude": 81.6296
  },
  "language": "en"
}

Response:

{
  "message": "Rain is likely tomorrow evening, with a 60% chance of rainfall.",
  "location": "Raipur",
  "language": "en",
  "weather_context": {
    "temperature": 28,
    "condition": "Cloudy",
    "rain_probability": 60
  },
  "sources": [
    "weather_api"
  ]
}

The frontend should only send the message,
location and language.

The backend handles:

- weather retrieval
- weather context
- prompt construction
- LLM interaction
- language handling
- response generation

Never expose API keys to the frontend.

## Supported Languages

Use:

en = English
hi = Hindi
te = Telugu
ta = Tamil
bn = Bengali
mr = Marathi
kn = Kannada
ml = Malayalam

## Location

The backend must eventually support:

city

and:

latitude + longitude

## Error Contract

Every API error must use:

{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message."
  }
}

Use:

400 = invalid request
404 = location not found
429 = rate limit
500 = server error

## CORS

Development frontend:

http://localhost:5173

CORS must be configurable through environment variables.

Do not hardcode production domains.

## Environment Variables

Secrets must only exist in backend environment variables.

Possible variables:

WEATHER_API_KEY=
LLM_API_KEY=
DATABASE_URL=
CORS_ORIGINS=

Never expose secrets to React.

Never commit .env.

## Development Strategy

IMPORTANT:

First implement everything using MOCK weather data and MOCK chatbot responses.

The frontend must be able to use:

GET /api/weather?city=Raipur

and:

POST /api/chat

without requiring real API keys.

Later replace the internal mock providers with real weather and LLM providers.

Do not change the frontend API contract when doing this.

## Architecture

Keep the backend modular.

Separate:

API routes
schemas
services
providers

The API response format is the contract.

Internal database/provider structures must never become the frontend contract.

## Frontend Independence

Do not import React code into the backend.

Do not create frontend-specific logic in the backend.

The backend communicates using JSON REST APIs.

## Important Rule

Never rename or remove an existing API field without explicitly informing the developer first.

Prefer backward-compatible changes.

Before making major architectural changes, explain them.