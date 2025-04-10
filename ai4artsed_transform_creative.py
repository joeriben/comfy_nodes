import random

class ai4artsed_transform_creative:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("transform_1", "transform_2", "transform_3", "transform_4")
    FUNCTION = "generate_transforms"
    CATEGORY = "AI4ArtsEd"

    def generate_transforms(self, text):
        transformations = [
            "Translate this text into the language of nature.",
            "Write this text as if it were part of a theatrical play.",
            "Phrase the text in the voice of a nostalgic robot.",
            "Turn the text into a rhythmic rap.",
            "Retell the same text as a fable with animals.",
            "Explain the content as if you're speaking to an alien.",
            "Write a philosophical version of this text.",
            "Compose an artistic interpretation of this text.",
            "Transform the text into a political speech.",
            "Make it into a scientific summary.",
            "Present the text as a cooking recipe.",
            "Write the text as a diary entry.",
            "Rewrite this text as if it were discovered in an ancient manuscript.",
            "Retell this message using only metaphors and symbols.",
            "Imagine this is a bedtime story for a post-human child.",
            "Present this as the internal monologue of a tree.",
            "Turn this text into the lyrics of a forgotten folk song.",
            "Render the text as an exchange of secret messages between spies.",
            "Write this as a protest chant at a fictional demonstration.",
            "Translate this into the dialect of a future underwater civilization.",
            "Rewrite the text as a conversation between extinct animals.",
            "Describe the content as an art critic reviewing an invisible artwork.",
            "Tell the story through the fragmented memories of a machine.",
            "Transform the text into an abstract painting using words only.",
            "Frame the message as a glitch in a virtual consciousness.",
            "Make it a dream sequence narrated by an unreliable narrator.",
            "Reframe the text as a recipe for emotional resilience.",
            "Retell it as an urban legend whispered in a digital back alley.",
            "Turn this text into an algorithm written in poetic form.",
            "Present it as a eulogy for a lost language."
        ]

        selected = random.sample(transformations, 4)
        outputs = [f"{instruction}\n\n{text}" for instruction in selected]
        return tuple(outputs)
