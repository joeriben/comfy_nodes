import os
from pathlib import Path


class OpenRouterKey:
    """Securely provides the OpenRouter API key to downstream nodes.

    The key is read **only** from a text file named ``openrouter.key`` that
    lives in the same directory as this node file.  The first non‑empty line
    of that file is treated as the key.  No environment variables, no hidden
    config files – one simple, explicit place.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_key"
    CATEGORY = "ai4artsed/utils"

    def get_key(self):
        key_path = Path(__file__).with_name("openrouter.key")
        if not key_path.exists():
            raise FileNotFoundError(
                "openrouter.key not found in the ai4artsed_comfyui folder.\n"
                "Create the file and paste your OpenRouter API key in the first line."
            )

        key = key_path.read_text(encoding="utf‑8").splitlines()[0].strip()
        if not key:
            raise ValueError("openrouter.key is empty – please paste your API key.")

        return (key,)


NODE_CLASS_MAPPINGS = {"OpenRouterKey": OpenRouterKey}
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenRouterKey": "Secure Access to OpenRouter API Key",
}
