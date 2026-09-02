from app.providers.mock_llm import MockLLMProvider, SUPPORTED_LANGUAGES
from app.schemas import ChatRequest, ChatResponse
from app.services.weather_service import create_chat_weather_context


def build_prompt(request: ChatRequest, weather_context: dict) -> str:
    return (
        "You are a weather assistant. Answer the user's question using only the "
        f"following weather context and respond in {SUPPORTED_LANGUAGES[request.language]}.\n"
        f"Location: {request.location.city}\n"
        f"User message: {request.message}\n"
        f"Weather context: {weather_context}"
    )


def generate_chat_response(
    request: ChatRequest, llm_provider: MockLLMProvider
) -> ChatResponse:
    weather_context = create_chat_weather_context(request.location.city)
    prompt = build_prompt(request, weather_context)
    message = llm_provider.generate(
        prompt, request.language, weather_context["rain_probability"]
    )
    return ChatResponse(
        message=message,
        location=request.location.city,
        language=request.language,
        weather_context=weather_context,
        sources=["weather_api"],
    )
