# Mock weather data for WeatherGPT.
# We are using fake data for now.
# Later, this can be replaced with a real weather API.


WEATHER_DATA = {
    "Raipur": {
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
}


FORECAST_DATA = {
    "Raipur": [

        {
            "date": "2026-09-02",
            "temperature_high": 30,
            "temperature_low": 25,
            "condition": "Cloudy",
            "rain_probability": 60
        },

        {
            "date": "2026-09-03",
            "temperature_high": 31,
            "temperature_low": 25,
            "condition": "Rainy",
            "rain_probability": 75
        },

        {
            "date": "2026-09-04",
            "temperature_high": 30,
            "temperature_low": 24,
            "condition": "Cloudy",
            "rain_probability": 55
        },

        {
            "date": "2026-09-05",
            "temperature_high": 32,
            "temperature_low": 25,
            "condition": "Partly Cloudy",
            "rain_probability": 35
        },

        {
            "date": "2026-09-06",
            "temperature_high": 33,
            "temperature_low": 26,
            "condition": "Sunny",
            "rain_probability": 15
        },

        {
            "date": "2026-09-07",
            "temperature_high": 32,
            "temperature_low": 25,
            "condition": "Cloudy",
            "rain_probability": 40
        },

        {
            "date": "2026-09-08",
            "temperature_high": 31,
            "temperature_low": 25,
            "condition": "Rainy",
            "rain_probability": 70
        }

    ]
}


ALERT_DATA = {
    "Raipur": [

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