import os
from pathlib import Path


class OpenRouterKey:
    """Securely provides the OpenRouter API key to downstream nodes.

    Priority order when resolving the key:
    1. Environment variable ``OPENROUTER_KEY``
    2. Text file ``openrouter.key`` located in the same folder as this node file
    The node outputs the key as a single STRING.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    # The node returns a single STRING – the API key
    RETURN_TYPES = ("STRING",)
    FUNCTION = "get_key"
    CATEGORY = "ai4artsed/utils"

    def get_key(self):
        """Return the OpenRouter API key following the priority rules."""
        # 1  Environment variable (highest priority)
        key = os.getenv("OPENROUTER_KEY", "").strip()

        # 2  Fallback: key file in the same directory
        if not key:
            key_file = Path(__file__).with_name("openrouter.key")
            if key_file.exists():
                key = key_file.read_text(encoding="utf-8").splitlines()[0].strip()

        # 3  If still empty → raise an explicit error
        if not key:
            raise ValueError(
                "OpenRouter API key not found.\n"
                "Set the environment variable 'OPENROUTER_KEY' OR create an 'openrouter.key' file "
                "in the same folder as 'openrouter_key.py'."
            )

        return (key,)


# ComfyUI registration ---------------------------------------------------------
NODE_CLASS_MAPPINGS = {
    "OpenRouterKey": OpenRouterKey,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenRouterKey": "Secure Access to OpenRouter API Key",
}
