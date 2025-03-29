import io
import base64
import requests
from PIL import Image

class OllamaPromptNode:
    # This attribute tells ComfyUI what type the node returns.
    RETURN_TYPES = ("STRING",)
    
    def __init__(self):
        self.stored_prompt = ""
    
    def execute(self, text, image: Image.Image = None, prompt_storage_key="my_ollama_prompt"):
        # If 'text' is not a string (e.g. CONDITIONING), convert it.
        if not isinstance(text, str):
            try:
                # Commonly, conditioning outputs are dictionaries with a "prompt" key.
                if isinstance(text, dict) and "prompt" in text:
                    text = text["prompt"]
                # Alternatively, if it's a list/tuple, take the first element.
                elif isinstance(text, (list, tuple)) and len(text) > 0:
                    text = str(text[0])
                else:
                    text = str(text)
            except Exception as e:
                print("Conversion error:", e)
                text = str(text)
        
        # Load or initialize the persistent prompt.
        if not self.stored_prompt:
            # Here, you might load from persistent storage.
            self.stored_prompt = "default prompt"
            # Optionally, store it using your own mechanism.
        
        # Combine the stored prompt with the incoming text.
        combined_prompt = f"{self.stored_prompt} {text}"
        payload = {
            "prompt": combined_prompt,
            "stream": False,
            "model": "gemma3",
        }
        
        # If an image is provided, encode it as Base64.
        if image is not None:
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
            payload["images"] = [encoded_image]
        else:
            payload["images"] = []
        
        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()
            result = response.json()
            generated_text = result.get("response", "")
        except Exception as e:
            print("Error communicating with Ollama:", e)
            generated_text = "Ollama Error"
        
        return (generated_text,)
    
    @classmethod
    def INPUT_TYPES(cls):
        # Accept both "STRING" and "CONDITIONING" for the 'text' input.
        return {
            "required": {
                "text": ("STRING", "CONDITIONING"),
                "prompt_storage_key": "STRING"
            },
            "optional": {
                "image": "IMAGE"
            }
        }
    
    @classmethod
    def OUTPUT_TYPES(cls):
        return {"text": "STRING"}
    
    @classmethod
    def FUNCTION(cls):
        return "execute"
    
    @classmethod
    def NODE_TITLE(cls):
        return "Ollama_Prompt"
    
    @classmethod
    def NODE_CATEGORY(cls):
        return "Custom_Nodes/Ollama"
    
    UI = {
        "text": {
            "label": "Input_Prompt",
            "type": "TEXT",
            "multiline": False,
            "default": ""
        },
        "image": {
            "label": "Input_Image",
            "type": "IMAGE"
        },
        "prompt_storage_key": {
            "label": "Prompt_Storage_Key",
            "type": "STRING",
            "default": "my_ollama_prompt"
        }
    }

# Registration in __init__.py:
# from .ollama_prompt import OllamaPromptNode
#
# NODE_CLASS_MAPPINGS = {
#     "OllamaPromptNode": OllamaPromptNode,
# }
#
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "OllamaPromptNode": "Ollama_Prompt",
# }

