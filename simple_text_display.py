class SimpleTextDisplay:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True, "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "display"
    CATEGORY = "Utils"

    def display(self, text):
        # Nur zurückgeben, damit es weitergeleitet werden kann
        return (text,)
