# AI4ArtsEd Prompt Nodes for ComfyUI

Experimental prompt transformation nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI), developed as part of the AI4ArtsEd research initiative. These components support stylistic and cultural translation of prompts and images for use in educational, artistic, and cultural research contexts.

More information: https://kubi-meta.de/ai4artsed

---

## 🔧 Features

- Accepts `STRING` or `IMAGE` input from any upstream node.
- Structured control of transformation via `style_prompt`, `context`, and `instruction`.
- Supports both:
  - **Local inference** using [Ollama](https://ollama.com/),
  - **Remote APIs** via [OpenRouter](https://openrouter.ai/).
- Produces output as `STRING` (for use in CLIP, chaining, or save/display).
- Optional debug logging and model unloading for Ollama.
- Optional API key file handling for OpenRouter.
- Includes an image-to-text analysis node for multimodal LLMs.
- New: **Flexible text distribution** node for routing strings to multiple downstream paths.

---

## 🧹 Available Nodes

### 1. `AI4ArtsEd Ollama Prompt`
→ Uses local Ollama models (GPU/CPU) for cultural prompt rewriting.

### 2. `AI4ArtsEd OpenRouter Prompt`
→ Uses hosted LLMs via OpenRouter for stylistic transformations.

### 3. `AI4ArtsEd OpenRouter ImageAnalysis`
→ Sends image input (as base64-encoded JPEG) to multimodal LLMs via OpenRouter (e.g. GPT-4V) with cultural-instruction prompts.

### 4. `AI4ArtsEd Text Distributor`
→ Distributes a text string to one or more of 12 outputs based on mode.

**Inputs:**
- `text`: Input string to be routed.
- `mode`: Distribution strategy — one of:
  - `"random"`: Sends to a randomly chosen output.
  - `"all"`: Sends to all outputs.
  - `"1"` to `"12"`: Sends to a specific output index.

**Outputs:**
- `text_1` to `text_12`: Routed outputs based on selected mode.

### 5. `AI4ArtsEd Text Remix`
→ Selectively or randomly combines 1–12 text inputs.

**Inputs:**
- `mode`: `"random"`, `"all"`, or `"1"`–`"12"`
- `text_1` to `text_12`: Optional style or instruction inputs

**Output:**
- `text`: Combined or selected text based on mode.

---

## 🔐 API Key Configuration (OpenRouter)

1. Manual: Enter API key in the `api_key` input field (masked).
2. File-based: Create `openrouter.key` in this node folder with your key on one line.

> `.gitignore` ensures this key is not versioned.

---

## 🚀 Installation

Use the ComfyUI Node Manager or clone the repo into your ComfyUI `custom_nodes` directory:

```bash
git clone https://github.com/yourusername/ai4artsed_comfyui.git
