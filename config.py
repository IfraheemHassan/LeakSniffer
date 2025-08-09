"""
Configuration settings for Leak Sniffer application
"""
import os

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "Test")

# Application Configuration
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "16"))
PAGE_TITLE = "Leak Search"
APP_TITLE = "🚀 Leak Sniffer"

# Search Configuration
DEFAULT_PROJECTION = {"_id": 0, "Domain": 1, "URL": 1, "Username": 1, "Password": 1}
COLUMN_ORDER = ["Domain", "URL", "Username", "Password"] 