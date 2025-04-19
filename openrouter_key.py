import os

class OpenRouterKey:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_key"
    CATEGORY = "ai4artsed/utils"

    def get_key(self):
        key = os.getenv("OPENROUTER_KEY", "")
        if not key:
            raise ValueError("Die Umgebungsvariable 'OPENROUTER_KEY' ist nicht gesetzt.")
        return (key,)

NODE_CLASS_MAPPINGS = {
    "OpenRouterKey": OpenRouterKey
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenRouterKey": "OpenRouter API Key from ENV"
}
