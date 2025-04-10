# ai4artsed_show_text.py
#
# Adapted from:
#   https://github.com/fairy-root/ComfyUI-Show-Text
#   Original author: fairy-root
#
# This file includes code licensed under the MIT License:
# --------------------------------------------------------
# MIT License
# Copyright (c) 2024 fairy-root
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction...
# [continue with full MIT license text]
#
# --------------------------------------------------------
# This adapted code is part of the AI4ArtsEd project,
# licensed under EUPL-1.2 where applicable.


class ai4artsed_show_text:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "AI4ArtsEd"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        if unique_id is not None and extra_pnginfo is not None:
            if not isinstance(extra_pnginfo, list):
                print("Error: extra_pnginfo is not a list")
            elif not isinstance(extra_pnginfo[0], dict) or "workflow" not in extra_pnginfo[0]:
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == str(unique_id[0])),
                    None,
                )
                if node:
                    node["widgets_values"] = [text]

        return {"ui": {"text": text}, "result": (text,)}
