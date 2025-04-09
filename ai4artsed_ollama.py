import requests

class ai4artsed_ollama:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "model": (cls._get_model_list(),),
                "system_prompt": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "run"
    CATEGORY = "AI4ArtsEd"

    @staticmethod
    def _get_model_list():
        try:
            res = requests.get("http://localhost:11434/api/tags", timeout=1)
            res.raise_for_status()
            models = res.json().get("models", [])
            model_names = [m["name"] for m in models]
            default_model = "gemma:7b" if "gemma:7b" in model_names else (model_names[0] if model_names else "gemma:7b")
            return ("STRING", {"default": default_model, "choices": model_names}) if model_names else ("STRING", {"default": "gemma:7b"})
        except:
            return ("STRING", {"default": "gemma:7b", "choices": ["gemma:7b"]})

    def run(self, prompt, model="gemma:7b", system_prompt=None):
        payload = {
            "model": model,
            "prompt": prompt,
            "system": system_prompt,
            "stream": False
        }

        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()
            result = response.json().get("response", "")
        except Exception as e:
            result = f"[Error from Ollama] {str(e)}"

        return (result,)
