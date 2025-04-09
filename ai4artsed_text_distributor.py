# filename: ai4artsed_text_distributor.py

import random

class ai4artsed_text_distributor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "mode": (
                    "STRING", {
                        "default": "random",
                        "choices": ["random", "all"] + [str(i) for i in range(1, 13)]
                    }
                ),
            }
        }

    RETURN_TYPES = ("STRING",) * 12
    RETURN_NAMES = [f"text_{i}" for i in range(1, 13)]
    FUNCTION = "distribute"
    CATEGORY = "AI4ArtsEd"

    def distribute(self, text, mode):
        outputs = [None] * 12

        if mode == "random":
            index = random.randint(0, 11)
            outputs[index] = text
        elif mode == "all":
            outputs = [text] * 12
        elif mode.isdigit() and 1 <= int(mode) <= 12:
            index = int(mode) - 1
            outputs[index] = text

        return tuple(outputs)
