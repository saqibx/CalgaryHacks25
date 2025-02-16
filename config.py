import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
    MONGO_URI = os.getenv("MONGO_URI")
    GEMINI_KEY = os.getenv("GEMINI_API_KEY")
