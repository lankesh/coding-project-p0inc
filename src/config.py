import os
from dotenv import load_dotenv, find_dotenv


# Check if .env file is present
dotenv_path = find_dotenv()

if dotenv_path:
    # Load environment variables from .env file
    load_dotenv()  # Load environment variables from a .env file

class Config:
    def __init__(self):
        self.calendar_adapter = os.getenv("CALENDAR_ADAPTER", "dummy")

config = Config()
