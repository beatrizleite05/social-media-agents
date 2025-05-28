import requests
from .config import IMAGE_API_KEY

VYRO_API_ENDPOINT = "https://api.vyro.ai/v2/image/generations"

def _placeholder(text):
    return f"https://via.placeholder.com/800x600.png?text={text.replace(' ','+')}"

def generate_image(prompt: str) -> str:
    if not IMAGE_API_KEY:
        return _placeholder(prompt[:40])
    
    try:
        # Prepare multipart/form-data payload
        files = {
            "prompt": (None, prompt),
            "style": (None, "minimalist"),  # Replace with valid style (e.g., "realistic")
            "aspect_ratio": (None, "1:1"),  # Optional: Change to "16:9", "9:16", etc.
        }
        
        headers = {
            "Authorization": f"Bearer {IMAGE_API_KEY}",
        }
        
        response = requests.post(
            VYRO_API_ENDPOINT,
            files=files,
            headers=headers,
            timeout=60
        )
        response.raise_for_status()  # Raise HTTP errors
        
        # Parse response (Vyro.ai returns JSON with an "image_url" field)
        return response.json().get("image_url") or _placeholder("image")
    
    except Exception as e:
        print(f"Imagine API error: {e}")
        return _placeholder("error")