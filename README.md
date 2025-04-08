# AI4ArtsEd Prompt Nodes for ComfyUI

Experimental nodes for ComfyUI. For more, see https\://kubi-meta.de/ai4artsed

These custom [ComfyUI](https://github.com/comfyanonymous/ComfyUI) nodes enable stylistic and cultural transformation of text prompts using either local LLMs via [Ollama](https://ollama.com/) or cloud-hosted models via [OpenRouter](https://openrouter.ai/). They are especially designed for multimodal pipelines in education, arts, and cultural research contexts.

---

## 🔧 Features

- Accept input from any upstream node producing `STRING` values.
- Combine it with a structured `style_prompt` and optional `context`.
- Perform transformation via:
  - **Ollama (local)** with GPU-backed models.
  - **OpenRouter (remote)** using external API.
- Return processed text as `STRING` output (suitable for chaining or CLIP encoding).
- Optional debug logging to inspect full prompts and LLM responses.
- Ollama node optionally unloads the model to free GPU memory.
- OpenRouter node optionally reads the API key from a file.

---

## 🧩 Available Nodes

### 1. `AI4ArtsEd Ollama Prompt`
For use with a local [Ollama](https://ollama.com/) installation (running on `localhost`).

#### 📥 Inputs
| Name           | Type   | Description                                                |
| -------------- | ------ | ---------------------------------------------------------- |
| `input_prompt` | STRING | Text to be transformed                                     |
| `input_context`| STRING | Additional semantic/aesthetic context                      |
| `style_prompt` | STRING | Instruction for the transformation                        |
| `url`          | STRING | Ollama server URL (default: `http://localhost:11434`)     |
| `model`        | STRING | Model identifier (dropdown, see source)                   |
| `debug`        | SELECT | Enable console output                                      |
| `unload_after` | SELECT | Unload the model after generation to free VRAM            |

#### 📤 Output
| Name     | Type   | Description                             |
| -------- | ------ | --------------------------------------- |
| `output` | STRING | The transformed/generated text response |

> IMPORTANT: You may chain multiple Ollama nodes. If you do so, **disable `unload_after` in all but the last one** to prevent GPU reloading delays.

---

### 2. `AI4ArtsEd OpenRouter Prompt`
For use with cloud-hosted models from [openrouter.ai](https://openrouter.ai).

#### 📥 Inputs
| Name           | Type   | Description                                                |
| -------------- | ------ | ---------------------------------------------------------- |
| `input_prompt` | STRING | Text to be transformed                                     |
| `input_context`| STRING | Additional semantic/aesthetic context                      |
| `style_prompt` | STRING | Instruction for the transformation                        |
| `api_key`      | STRING | OpenRouter API key (masked field)                          |
| `model`        | STRING | Model identifier (dropdown, see source)                   |
| `debug`        | SELECT | Enable console output                                      |

#### 📤 Output
| Name     | Type   | Description                             |
| -------- | ------ | --------------------------------------- |
| `output` | STRING | The transformed/generated text response |

---

## 🔐 API Key Configuration (OpenRouter)

This node requires an API key for access to [openrouter.ai](https://openrouter.ai). There are two options for providing it:

### 1. Enter manually (recommended for debugging)
Paste your key into the `api_key` field of the node. The input will be masked in the UI.

### 2. Use a local file
Create a file named `openrouter.key` in the same folder as the node (typically `ComfyUI/custom_nodes/ai4artsed_comfyui/`). The file should contain only the API key as a single line (no quotes, no newline).

> The file is automatically ignored by Git via `.gitignore`.

---

## 🚀 Installation

Place this repository inside your `ComfyUI/custom_nodes/` directory:

```bash
git clone https://github.com/yourusername/ai4artsed_comfyui.git
```

Then restart ComfyUI.

OR

Use the ComfyUI Node Manager!

Make sure that:
- Ollama is running locally (if used).
- Your OpenRouter API key is configured.

---

