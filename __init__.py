from .ollama_prompt import ai4artsed_ollama
from .simple_text_display import SimpleTextDisplay

NODE_CLASS_MAPPINGS = {
    "ai4artsed_ollama": ai4artsed_ollama,
    "SimpleTextDisplay": SimpleTextDisplay,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ai4artsed_ollama": "AI4ArtsEd Ollama Prompt",
    "SimpleTextDisplay": "Simple Text Display",
}
