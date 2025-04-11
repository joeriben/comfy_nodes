class ShowText:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "pass_through"
    OUTPUT_NODE = True
    CATEGORY = "AI4ArtsEd"

    def pass_through(self, text):
        print(f"[ShowText] {text}")
        return {"ui": {"text": text}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ShowText": ShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText": "Show Text",
}
