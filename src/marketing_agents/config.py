import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
DEFAULT_MODEL = "gemini-2.0-flash"
MAX_HASHTAGS = 10

IMAGE_API_KEY = os.getenv("IMAGE_API_KEY", "")

INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN", "")
INSTAGRAM_PAGE_ID = os.getenv("INSTAGRAM_PAGE_ID", "")
LINKEDIN_ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
LINKEDIN_ORG_ID = os.getenv("LINKEDIN_ORG_ID", "")

TIMEZONE = os.getenv("TIMEZONE", "Europe/Lisbon")
POST_HOUR = int(os.getenv("POST_HOUR", 15)) # Default to 15 (3 PM)