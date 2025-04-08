import torch
import numpy as np
import base64
import requests
import json
from io import BytesIO
from PIL import Image

class ai4artsed_openrouter_imageanalysis:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "query": ("STRING", {
                    "multiline": True,
                    "default": "Describe the image. Detect its likely cultural context. Enrich your description with analyses of the cultural constellations and meanings, relations, values expressed in the image."
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "model": ([
                    "openai/gpt-4o",
                    "meta-llama/llama-4-maverick",
                    "microsoft/phi-4-multimodal-instruct",
                    "google/gemini-flash-1.5"
                ],),
                "max_tokens": ("INT", {
                    "default": 1024, "min": 1, "max": 8192
                }),
                "temperature": ("FLOAT", {
                    "default": 0.7, "min": 0.0, "max": 1.0
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "analyze"
    CATEGORY = "ai4artsed"

    def analyze(self, images, query, api_key, model, max_tokens, temperature):
        encoded_images = []

        for image in images:
            array = image.cpu().numpy()
            array = (array * 255).clip(0, 255).astype(np.uint8)

            if array.shape[0] == 1:
                image_np = array[0]
            elif array.shape[0] == 3:
                image_np = np.transpose(array, (1, 2, 0))
            else:
                raise ValueError("Unsupported image shape: expected 1 or 3 channels.")

            pil_image = Image.fromarray(image_np)
            buffer = BytesIO()
            pil_image.save(buffer, format="PNG")
            encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")

            encoded_images.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{encoded}"
                }
            })

        messages = [{
            "role": "user",
            "content": [{"type": "text", "text": query}] + encoded_images
        }]

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        body = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                data=json.dumps(body),
                timeout=60
            )
            response.raise_for_status()
            data = response.json()
            return (data["choices"][0]["message"]["content"],)
        except Exception as e:
            return (f"[ERROR] {str(e)}",)
