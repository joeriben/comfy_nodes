class ai4artsed_show_text:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "show"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "AI4ArtsEd"

    def show(self, text):
        return {"ui": {"text": text}, "result": (text,)}


NODE_CLASS_MAPPINGS = {
    "ai4artsed_show_text": ai4artsed_show_text,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ai4artsed_show_text": "Show Text",
}
