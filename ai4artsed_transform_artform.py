import random

class ai4artsed_transform_artform:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("artform_1", "artform_2", "artform_3", "artform_4")
    FUNCTION = "generate_artforms"
    CATEGORY = "AI4ArtsEd"

    def generate_artforms(self, text):
        artforms = [
            "Rewrite this in the style of Japanese Noh theatre.",
            "Render the text as a Yoruba praise poem.",
            "Transform this into a piece of spoken word poetry.",
            "Write this in the spirit of German Expressionist cinema.",
            "Reframe this message using techniques of Cubism.",
            "Tell this story like an episode of Indian epic theatre.",
            "Compose the text as if it were a fragment of a Maori chant.",
            "Turn this into a surrealist manifesto.",
            "Express this as a scene from a South Korean melodrama.",
            "Adapt this into an Afro-futurist myth.",
            "Tell the story through the rhythm of a Capoeira song.",
            "Render this as instructions from a Bauhaus design manual.",
            "Retell this using traditional Inuit oral storytelling.",
            "Phrase this message like a painting by Frida Kahlo.",
            "Reimagine this as part of a Chinese ink wash painting.",
            "Write this as tango lyrics from Buenos Aires.",
            "Shape the message as a Tibetan prayer wheel invocation.",
            "Turn this into a myth from the Quechua tradition.",
            "Interpret the text in the mood of Scandinavian noir.",
            "Transform this into a Mexican altar offering (ofrenda).",
            "Present this as a scene from a Nigerian Nollywood drama.",
            "Retell this message in the format of a West African griot tale.",
            "Convert this into an Egyptian hieroglyphic inscription.",
            "Express the content through Aboriginal Australian dot painting.",
            "Rephrase this in the tone of a medieval Persian miniature story.",
            "Translate the message into the aesthetics of glitch art.",
            "Present this like a jazz improvisation.",
            "Reframe it as a scene from Italian neorealism.",
            "Adapt this into an avant-garde performance script.",
            "Transform the text into a Haitian Vodou ceremonial chant."
        ]

        selected = random.sample(artforms, 4)
        outputs = [f"{instruction}\n\n{text}" for instruction in selected]
        return tuple(outputs)
