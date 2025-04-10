from .ai4artsed_ollama import ai4artsed_ollama
from .ai4artsed_ollama_imageanalysis import ai4artsed_ollama_imageanalysis
from .ai4artsed_openrouter import ai4artsed_openrouter
from .ai4artsed_openrouter_imageanalysis import ai4artsed_openrouter_imageanalysis
from .ai4artsed_text_remix import ai4artsed_text_remix
from .ai4artsed_text_transform_creative import ai4artsed_text_transform_creative
from .ai4artsed_text_transform_artform import ai4artsed_text_transform_artform

NODE_CLASS_MAPPINGS = {
    "ai4artsed_ollama": ai4artsed_ollama,
    "ai4artsed_ollama_imageanalysis": ai4artsed_ollama_imageanalysis,
    "ai4artsed_openrouter": ai4artsed_openrouter,
    "ai4artsed_openrouter_imageanalysis": ai4artsed_openrouter_imageanalysis,
    "ai4artsed_text_remix": ai4artsed_text_remix,
    "ai4artsed_text_transform_creative": ai4artsed_text_transform_creative,
    "ai4artsed_text_transform_artform": ai4artsed_text_transform_artform,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ai4artsed_ollama": "AI4ArtsEd Ollama Promptinterception",
    "ai4artsed_ollama_imageanalysis": "AI4ArtsEd Ollama Image Analysis",
    "ai4artsed_openrouter": "AI4ArtsEd OpenRouter Promptinterception",
    "ai4artsed_openrouter_imageanalysis": "AI4ArtsEd OpenRouter Image Analysis",
    "ai4artsed_text_remix": "AI4ArtsEd Text Remix",
    "ai4artsed_text_transform_creative": "Text Transform Creative",
    "ai4artsed_text_transform_artform": "Text Transform Artform",
}
