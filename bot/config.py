import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram ID админа (твой ID)
ADMIN_IDS = {123456789}
