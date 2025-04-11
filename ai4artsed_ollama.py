import requests

class ai4artsed_ollama:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "system_prompt": ("STRING", {
                    "default": "Translate the prompt according to the context. Translate epistemic, cultural, and aesthetic, as well as value-related contexts.\n\nContext:\n",
                    "multiline": True
                }),
                "model": ([
                    "mistral:7b",
                    "gemma3:27b",
                    "deepseek-r1:32b",
                    "deepseek-r1:14b",
                    "exaone-deep:32b"
                ],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "run"
    CATEGORY = "AI4ArtsEd"

    def run(self, prompt, system_prompt, model):
        # Optional: Custom formatting logic if system_prompt uses placeholders
        system_msg = f"{system_prompt.strip()}"

        payload = {
            "model": model,
            "prompt": prompt,
            "system": system_msg,
            "stream": False
        }

        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()
            result = response.json().get("response", "")
        except Exception as e:
            result = f"[Error from Ollama] {str(e)}"

        return (result,)
