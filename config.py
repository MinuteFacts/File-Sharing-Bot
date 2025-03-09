import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.getenv("BOT_TOKEN", "7896862118:AAHOjDVxICwYSdfDEwioqkQ2Dk6sZuKcfzQ")
API_ID = int(os.getenv("API_ID", "16978078"))
API_HASH = os.getenv("API_HASH", "91ccaf748f031b656bbf64ff47f990e3")

OWNER_ID = int(os.getenv("OWNER_ID", "1077880102"))
DB_URL = os.getenv("DB_URL", "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001847420676"))  # Removed extra space
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", "-1002358532189"))
FORCE_SUB_CHANNEL2 = int(os.getenv("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.getenv("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.getenv("FORCE_SUB_CHANNEL4", "0"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900"))

PORT = int(os.getenv("PORT", "8080"))  # Ensure it's an integer
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

# Admin Handling
try:
    ADMINS = {6848088376, OWNER_ID}  # Use a set to prevent duplicates
    ADMINS.update(map(int, os.getenv("ADMINS", "6848088376").split()))
    ADMINS = list(ADMINS)  # Convert back to a list
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", "<b>@Animes2u - {file_name}</b>")

PROTECT_CONTENT = os.getenv('PROTECT_CONTENT', "True").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.getenv('DISABLE_CHANNEL_BUTTON', "True").lower() == "true"

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.getenv("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")
FORCE_MSG = os.getenv("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
