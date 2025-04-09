import base64
import requests
import io
from PIL import Image

class ai4artsed_ollama_imageanalysis:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {"multiline": True}),
                "model": (cls._get_model_list(),),
                "info": ("STRING", {
                    "default": "💡 Only models like 'llava', 'llava-1.5', or 'bakllava' support image inputs in Ollama.",
                    "multiline": True
                }),
            },
            "optional": {
                "system_prompt": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "analyze"
    CATEGORY = "AI4ArtsEd"

    @staticmethod
    def _get_model_list():
        try:
            res = requests.get("http://localhost:11434/api/tags", timeout=1)
            res.raise_for_status()
            models = res.json().get("models", [])
            model_names = [m["name"] for m in models]
            return ("STRING", {"default": model_names[0], "choices": model_names}) if model_names else ("STRING", {"default": "llava"})
        except:
            return ("STRING", {"default": "llava", "choices": ["llava"]})

    def analyze(self, image, prompt, model="llava", info=None, system_prompt=None):
        img_pil = Image.fromarray((image[0] * 255).astype("uint8"))
        buffer = io.BytesIO()
        img_pil.save(buffer, format="JPEG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        payload = {
            "model": model,
            "prompt": prompt,
            "images": [img_base64],
            "stream": False
        }

        if system_prompt:
            payload["system"] = system_prompt

        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()
            output = response.json().get("response", "")
        except Exception as e:
            output = f"[Error from Ollama] {str(e)}"

        return (output,)
