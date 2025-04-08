from .ai4artsed_ollama import ai4artsed_ollama
from .ai4artsed_openrouter import ai4artsed_openrouter

NODE_CLASS_MAPPINGS = {
    "ai4artsed_ollama": ai4artsed_ollama,
    "ai4artsed_openrouter": ai4artsed_openrouter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ai4artsed_ollama": "AI4ArtsEd Ollama Promptinterception",
    "ai4artsed_openrouter": "AI4ArtsEd OpenRouter Promptinterception",
}
