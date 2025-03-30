# AI4ArtsEd Ollama Prompt Node

Experimental nodes for ComfyUI. For more, see https\://kubi-meta.de/ai4artsed

A custom [ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for stylistic and cultural transformation of input text using local LLMs served via [Ollama](https://ollama.com/).

This node allows you to combine a free-form prompt (e.g. translation, poetic recoding, genre shift) with externally supplied text in the ComfyUI graph. The result is processed via an Ollama-hosted model and returned as plain text.

IMPORTANT: You may chain two or more instances of this node. If you do so, make sure to deactivate "unload_after" in every instance but the last one. (You probably want to unload Ollama after the task in order to have enough GPU memory for your text2image-Model.)

---

## 🔧 Features

- Receives text input from other nodes (e.g. primitives, outputs, chains).
- Adds a static instruction prompt to guide the transformation.
- Sends the composed prompt to a specified model via Ollama.
- Selectable model from dropdown (configurable in source).
- Optional debug output to inspect prompt and response.
- Optionally unloads the Ollama model after inference to free GPU memory.

---

## 📥 Inputs

| Name           | Type   | Description                                                |
| -------------- | ------ | ---------------------------------------------------------- |
| `input_text`   | STRING | Text input from another node (e.g. Primitive or Prompt)    |
| `style_prompt` | STRING | Instruction for how to transform the input (in-node field) |
| `url`          | STRING | Ollama server URL (default: `http://localhost:11434`)      |
| `model`        | STRING | Selected model (dropdown: see source)                      |
| `debug`        | SELECT | "enable" or "disable" console output for debugging         |
| `unload_after` | SELECT | "enable" to unload the model after inference               |

---

## 📤 Output

| Name     | Type   | Description                             |
| -------- | ------ | --------------------------------------- |
| `output` | STRING | The transformed/generated text response |

---

## 🚀 Installation

Place this repository inside your `ComfyUI/custom_nodes/` directory:

```bash
git clone https://github.com/yourusername/ai4artsed_ollama.git
```

Then restart ComfyUI.

