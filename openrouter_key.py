from .openrouter_key import OpenRouterKey   # ➊ import

NODE_CLASS_MAPPINGS.update({
    "OpenRouterKey": OpenRouterKey,          # ➋ registrieren
})

NODE_DISPLAY_NAME_MAPPINGS.update({
    "OpenRouterKey": "Secure Access to OpenRouter API Key",
})
