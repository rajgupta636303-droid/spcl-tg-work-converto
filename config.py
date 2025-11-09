import os
from dotenv import load_dotenv

# Load .env file (for local development)
load_dotenv()

# Bot token - reads from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is not set!")

# Temp folder path
TEMP_DIR = 'temp'

# Supported image formats
SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif', 'tiff']

# Maximum file size (bytes) - 20MB
MAX_FILE_SIZE = 20 * 1024 * 1024
