from ollama import Client
from pprint import pprint

class OllamaTransform:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Enter your prompt here."}),
                "transformation": (["Translate to Indigenous Language", "Dadaistic Artwork Inspiration"],),
                "url": ("STRING", {"multiline": False, "default": "http://127.0.0.1:11434"}),
                "model": ((), {}),  # leave empty or set to a default model identifier as required
                "debug": (["enable", "disable"],)
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    FUNCTION = "ollama_transform"
    CATEGORY = "Ollama"

    def ollama_transform(self, text, transformation, url, model, debug):
        # Determine the fixed instruction based on the chosen transformation type.
        if transformation == "Translate to Indigenous Language":
            instruction = (
                "Translate and culturally transform the following text into an indigenous language, "
                "ensuring that traditional cultural nuances are preserved: "
            )
        elif transformation == "Dadaistic Artwork Inspiration":
            instruction = (
                "Interpret the following text as inspiration for an authentic dadaistic artwork, "
                "emphasizing abstraction, spontaneity, and non-traditional aesthetics: "
            )
        else:
            instruction = ""

        # Combine the instruction with the original text prompt.
        full_prompt = instruction + "\n" + text

        # Create a client to connect to the Ollama server.
        client = Client(host=url)

        # Send the combined prompt to Ollama.
        response = client.generate(model=model, prompt=full_prompt, keep_alive="5m", format="")

        # If debug mode is enabled, output detailed diagnostic information.
        if debug == "enable":
            print("[Ollama Transform] Debug Info:")
            print("Full Prompt Sent to Ollama:")
            print(full_prompt)
            print("Response Received:")
            pprint(response)

        # Return the generated response text.
        return (response.get('response', ''),)
