import numpy as np
from typing import Any

class ai4artsed_show_text:
    """
    A node for displaying text inputs within the ComfyUI interface.
    Accepts various data types and presents them as readable strings.
    """

    @classmethod
    def INPUT_TYPES(cls):
        """
        Defines the input types for the node.
        """
        return {
            "required": {
                "text_input": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "show_text"
    OUTPUT_NODE = True
    CATEGORY = "AI4ArtsEd"

    def show_text(self, text_input: Any):
        """
        Processes the input and prepares it for display in the UI.

        Args:
            text_input (Any): The input data to be displayed.

        Returns:
            dict: A dictionary containing the UI display data.
        """
        # Ensure text_input is a string for consistent display
        if not isinstance(text_input, str):
            text_input = str(text_input)

        # Prepare the data for UI display
        return {"ui": {"text": text_input}}
