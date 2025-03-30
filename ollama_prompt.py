import io
import base64
import requests
from PIL import Image

class OllamaPromptNode:
    RETURN_TYPES = ("STRING",)
    
    def __init__(self):
        self.stored_prompt = ""
    
    def execute(self, text, image: Image.Image = None, prompt_storage_key=None):
        # Use default if prompt_storage_key is not provided
        if not prompt_storage_key:
            prompt_storage_key = "my_ollama_prompt"
        
        # Convert text if needed (handles CONDITIONING type)
        if not isinstance(text, str):
            try:
                if isinstance(text, dict) and "prompt" in text:
                    text = text["prompt"]
                elif isinstance(text, (list, tuple)) and len(text) > 0:
                    text = str(text[0])
                else:
                    text = str(text)
            except Exception as e:
                print("Conversion error:", e)
                text = str(text)
        
        # Load or initialize the persistent prompt.
        if not self.stored_prompt:
            self.stored_prompt = "default prompt"
            # Optionally, store it using your persistent storage mechanism.
        
        # Combine stored prompt with input text.
        combined_prompt = f"{self.stored_prompt} {text}"
        payload = {
            "prompt": combined_prompt,
            "stream": False,
            "model": "gemma3",
        }
        
        # Process image input, if available.
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
        return {
            "required": {
                "text": ("STRING", "CONDITIONING"),
            },
            "optional": {
                "prompt_storage_key": "STRING",  # Optional, defaults to "my_ollama_prompt" if not connected.
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
        "prompt_storage_key": {
            "label": "Prompt_Storage_Key",
            "type": "STRING",
            "default": "my_ollama_prompt"
        },
        "image": {
            "label": "Input_Image",
            "type": "IMAGE"
        }
    }

# In your __init__.py for the package, register the node:
#
# from .ollama_prompt import OllamaPromptNode
#
# NODE_CLASS_MAPPINGS = {
#     "OllamaPromptNode": OllamaPromptNode,
# }
#
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "OllamaPromptNode": "Ollama_Prompt",
# }
