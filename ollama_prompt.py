import io
import base64
import requests
from PIL import Image

class OllamaPromptNode:
    # Required static properties for ComfyUI
    class_type = "OllamaPromptNode"
    RETURN_TYPES = ("STRING",)
    INPUT_TYPES = {
        "required": {
            "text": ("STRING", "CONDITIONING")
        },
        "optional": {
            "image": "IMAGE"
        }
    }
    OUTPUT_TYPES = {"text": "STRING"}
    FUNCTION = "execute"
    NODE_TITLE = "Ollama_Prompt"
    NODE_CATEGORY = "ai4artsed"  # Changed to your requested category

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
        }
    }
    
    def __init__(self):
        self.stored_prompt = "default prompt"
    
    def execute(self, text, image: Image.Image = None):
        # If 'text' is not a string, convert it.
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
        
        # Combine the stored prompt with the incoming text.
        combined_prompt = f"{self.stored_prompt} {text}"
        payload = {
            "prompt": combined_prompt,
            "stream": False,
            "model": "gemma3",
        }
        
        # Process the optional image input.
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

# __init__.py registration file (in the same custom node folder) should contain:
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
