from typing import Dict

SUPPORTED_LANGUAGES = {
    "en": "English",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "bn": "Bengali",
    "mr": "Marathi",
    "kn": "Kannada",
    "ml": "Malayalam",
}


class MockLLMProvider:
    """Deterministic stand-in for a future real LLM provider."""

    def generate(self, prompt: str, language: str, rain_probability: float) -> str:
        del prompt
        responses: Dict[str, str] = {
            "en": f"Rain is likely tomorrow evening, with a {rain_probability:g}% chance of rainfall.",
            "hi": f"कल शाम बारिश की संभावना है, और बारिश की {rain_probability:g}% संभावना है।",
            "te": f"రేపు సాయంత్రం వర్షం పడే అవకాశం ఉంది, వర్షపాతం అవకాశం {rain_probability:g}% ఉంది.",
            "ta": f"நாளை மாலை மழை பெய்ய வாய்ப்புள்ளது, மழைக்கான வாய்ப்பு {rain_probability:g}%.",
            "bn": f"আগামীকাল সন্ধ্যায় বৃষ্টির সম্ভাবনা রয়েছে, বৃষ্টির সম্ভাবনা {rain_probability:g}%.",
            "mr": f"उद्या संध्याकाळी पावसाची शक्यता आहे, पावसाची शक्यता {rain_probability:g}% आहे.",
            "kn": f"ನಾಳೆ ಸಂಜೆ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ, ಮಳೆಯ ಸಾಧ್ಯತೆ {rain_probability:g}% ಇದೆ.",
            "ml": f"നാളെ വൈകുന്നേരം മഴയ്ക്ക് സാധ്യതയുണ്ട്, മഴയുടെ സാധ്യത {rain_probability:g}% ആണ്.",
        }
        return responses[language]
