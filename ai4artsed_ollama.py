import requests

class ai4artsed_ollama:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_prompt": ("STRING", {"forceInput": True, "multiline": True}),
                "input_context": ("STRING", {"forceInput": True, "multiline": True}),
                "style_prompt": ("STRING", {
                    "default": "Translate the prompt according to the context. Translate epistemic, cultural, and aesthetic, as well as value-related contexts.",
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

    def run(self, input_prompt, input_context, style_prompt, model):
        system_prompt = f"{style_prompt}\n\nContext:\n{input_context}"
        payload = {
            "model": model,
            "prompt": input_prompt,
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
