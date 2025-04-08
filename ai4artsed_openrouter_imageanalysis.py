"""
ai4artsed_openrouter_imageanalysis.py

This node analyzes an input image by first ensuring that the image data is in the expected CHW format.
If the input image is in HWC format (i.e. the channels are given in the last dimension), it transposes
the array accordingly. The node then encodes the image and sends it to the OpenRouter image analysis API.
"""

import numpy as np
import torch
import requests
import json
import cv2
import base64

class ai4artsed_openrouter_imageanalysis:
    def __init__(self, aux_id=None, ver=None):
        # Store auxiliary identifiers and version numbers if needed for the API
        self.aux_id = aux_id
        self.ver = ver

    def analyze(self, images, **kwargs):
        """
        Analyzes the given image(s). Expects the first image in the list (or a single image)
        in a tensor, numpy array, or image-like format.

        This function ensures that the image array is in CHW format.
        If not, and if the last dimension is one of (1, 3, 4), a transpose from HWC to CHW is applied.
        """
        # Use the first image if a list is provided
        if isinstance(images, list):
            if not images:
                raise ValueError("No images provided for analysis.")
            image = images[0]
        else:
            image = images

        # Convert image to a numpy array if necessary
        if isinstance(image, torch.Tensor):
            # Detach and move to CPU if needed
            array = image.cpu().detach().numpy()
        elif not isinstance(image, np.ndarray):
            array = np.array(image)
        else:
            array = image

        # Check dimensionality and ordering:
        if array.ndim == 3:
            # If the first dimension is not one of (1, 3, or 4) but the last is,
            # we assume the image is in HWC format and transpose it to CHW.
            if array.shape[0] not in (1, 3, 4) and array.shape[-1] in (1, 3, 4):
                array = array.transpose(2, 0, 1)

        # Verify that the resulting array now has the channel dimension as the first axis.
        if array.ndim < 3 or array.shape[0] not in (1, 3, 4):
            raise ValueError(f"Unsupported image shape: expected 1, 3, or 4 channels, got {array.shape[0]}")

        # Proceed with the image analysis process.
        encoded_image = self.encode_image(array)
        response = self.send_image_analysis_request(encoded_image)
        return response

    def encode_image(self, array):
        """
        Encodes the image array into a base64-encoded JPEG.
        First, converts from CHW to HWC format for cv2 encoding.
        """
        # Convert from CHW to HWC for cv2
        array_for_encoding = array.transpose(1, 2, 0)
        
        # Ensure the array is in the proper uint8 range:
        if array_for_encoding.dtype != np.uint8:
            # Scale the array values to [0, 255] if needed.
            array_for_encoding = np.clip(array_for_encoding, 0, 1)
            array_for_encoding = (array_for_encoding * 255).astype(np.uint8)
        
        # Encode the image as JPEG
        success, buffer = cv2.imencode('.jpg', array_for_encoding)
        if not success:
            raise ValueError("Failed to encode image as JPEG.")
        jpg_as_text = base64.b64encode(buffer).decode('utf-8')
        return jpg_as_text

    def send_image_analysis_request(self, encoded_image):
        """
        Sends the base64-encoded image to the OpenRouter API for analysis.
        Replace the URL and adjust the payload as required by the API.
        """
        url = "https://api.openrouter.ai/analysis"  # This URL is a placeholder.
        payload = {
            "image": encoded_image,
            "aux_id": self.aux_id,
            "ver": self.ver
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"Failed to analyze image, status code {response.status_code}, response: {response.text}")
