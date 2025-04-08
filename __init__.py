from .ollama_prompt import ai4artsed_ollama
from .ollama_prompt_openrouter import ai4artsed_openrouter

NODE_CLASS_MAPPINGS = {
    "ai4artsed_ollama": ai4artsed_ollama,
    "ai4artsed_openrouter": ai4artsed_openrouter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ai4artsed_ollama": "AI4ArtsEd Ollama Prompt",
    "ai4artsed_openrouter": "AI4ArtsEd OpenRouter Prompt",
}
