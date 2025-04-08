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

---

## 🧹 Available Nodes

### 1. `AI4ArtsEd Ollama Prompt`
→ Uses local Ollama models (GPU/CPU) for cultural prompt rewriting.

### 2. `AI4ArtsEd OpenRouter Prompt`
→ Uses hosted LLMs via OpenRouter for stylistic transformations.

### 3. `AI4ArtsEd OpenRouter ImageAnalysis`
→ Sends image input (as base64-encoded JPEG) to multimodal LLMs via OpenRouter (e.g. GPT-4V) with cultural-instruction prompts.

---

## 🔐 API Key Configuration (OpenRouter)

1. Manual: Enter API key in the `api_key` input field (masked).
2. File-based: Create `openrouter.key` in this node folder with your key on one line.

> `.gitignore` ensures this key is not versioned.

---

## 🚀 Installation

Use the ComyUI Node Manager or clone the repo into your ComfyUI custom_nodes directory:

```bash
git clone https://github.com/yourusername/ai4artsed_comfyui.git
```

Restart ComfyUI or use the Node Manager.

Make sure:
- Ollama is running locally (if used).
- Your OpenRouter API key is configured.

---

## 📄 License

This project is licensed under the **European Union Public License (EUPL) v1.2**.  
It guarantees public access and commons-based reuse under strong copyleft terms.

Full license text: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12  
See `LICENSE` and the German summary inside for more information.

---

### 📜 Third-party code

Parts of the code in `ai4artsed_openrouter_imageanalysis.py` are adapted from the  
[ComfyUI Ollama project by stavsap](https://github.com/stavsap/comfyui-ollama),  
licensed under the Apache License 2.0.

See `THIRD_PARTY_LICENSES/comfyui-ollama_APACHE.txt` for full details.

---
