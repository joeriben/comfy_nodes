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
