import os
import requests
import json

class ai4artsed_openrouter:
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
                "api_key": ("STRING", {"multiline": False, "password": True}),
                "model": ([
                    "mistralai/mistral-7b-instruct",
                    "meta-llama/llama-2-13b-chat",
                    "openchat/openchat-3.5",
                    "google/gemma-7b-it",
                    "gryphe/mythomax-l2-13b"
                ],),
                "debug": (["enable", "disable"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run"
    CATEGORY = "AI4ArtsEd"

    def get_api_key(self, user_input_key):
        if user_input_key.strip():
            return user_input_key.strip()

        # Suche im selben Verzeichnis wie dieses Skript
        key_path = os.path.join(os.path.dirname(__file__), "openrouter.key")
        try:
            with open(key_path, "r") as f:
                return f.read().strip()
        except Exception:
            raise Exception("[AI4ArtsEd OpenRouter Node] No API key provided and openrouter.key not found.")

    def run(self, input_prompt, input_context, style_prompt, api_key, model, debug):
        full_prompt = f"Task:\n{style_prompt.strip()}\n\nContext:\n{input_context.strip()}\nPrompt:\n{input_prompt.strip()}"

        messages = [
            {"role": "system", "content": "You are a fresh assistant instance. Forget all previous conversation history."},
            {"role": "user", "content": full_prompt}
        ]

        headers = {
            "Authorization": f"Bearer {self.get_api_key(api_key)}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": messages,
            "temperature": 0.7
        }

        url = "https://openrouter.ai/api/v1/chat/completions"
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        if response.status_code != 200:
            raise Exception(f"[AI4ArtsEd OpenRouter Node] API Error: {response.status_code}\n{response.text}")

        result = response.json()
        output_text = result["choices"][0]["message"]["content"]

        if debug == "enable":
            print(">>> AI4ARTSED OPENROUTER NODE <<<")
            print("Model:", model)
            print("Prompt sent:\n", full_prompt)
            print("Response received:\n", output_text)

        return (output_text,)
