from ollama import Client
from pprint import pprint
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
                "url": ("STRING", {"default": "http://localhost:11434"}),
                "model": (["mistral:7b", "gemma3:27b", "deepseek-r1:32b", "deepseek-r1:14b", "exaone-deep:32b"],),
                "debug": (["enable", "disable"],),
                "unload_after": (["enable", "disable"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run"
    CATEGORY = "AI4ArtsEd"

    def run(self, input_prompt, input_context, style_prompt, url, model, debug, unload_after):
        full_prompt = f"Task:\n{style_prompt.strip()}\n\nContext:\n{input_context.strip()}\nPrompt:\n{input_prompt.strip()}"

        client = Client(host=url)

        # Anfrage an Modell mit explizitem Systemprompt (Kontextreset)
        response = client.generate(
            model=model,
            prompt=full_prompt,
            keep_alive="5m",
            format="",
            system="You are a fresh assistant instance. Forget all previous conversation history."
        )

        if debug == "enable":
            print(">>> AI4ARTSED OLLAMA NODE <<<")
            print("Model:", model)
            print("Prompt sent:\n", full_prompt)
            print("Response received:\n", response.get("response", ""))

        # Modell ggf. entladen
        if unload_after == "enable":
            try:
                unload_url = url.rstrip("/") + "/api/unload"
                res = requests.post(unload_url, json={"model": model})
                if debug == "enable":
                    print(f"Model '{model}' unloaded. Status: {res.status_code}")
            except Exception as e:
                print(f"[AI4ArtsEd Ollama Node] Unload failed: {e}")

        return (response.get("response", ""),)
