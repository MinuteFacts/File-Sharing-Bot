import os
import logging
from logging.handlers import RotatingFileHandler

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7896862118:AAHOjDVxICwYSdfDEwioqkQ2Dk6sZuKcfzQ")
API_ID = int(os.environ.get("API_ID", "979826"))
API_HASH = os.environ.get("API_HASH", "238183386c30590d073b457166ba260d")

# Owner & Database
OWNER_ID = int(os.environ.get("OWNER_ID", "1077880102"))
DB_URL = os.environ.get(
    "DB_URL",
    "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# Force Subscription Channels
CHANNEL_IDS = [
    "-1002358588449",  # Required to join
    "-1001657207796",  # Suggested
    "-1002399437916"   # Suggested
]
FORCE_SUB_CHANNEL = CHANNEL_IDS[0]  # First one is mandatory
REQUESTED_JOIN_CHANNELS = CHANNEL_IDS[1:]  # Others are suggested

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900"))  # Auto-delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admins list handling
try:
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "6848088376").split()]
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

ADMINS.extend([1077880102, 6848088376])

# Customizations
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>@Animes2u - {file_name}</b>")
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "True") == "True"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == "True"
BOT_STATS_TEXT = "<b>BOT UPTIME:</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Don't Send Me Messages Directly. I'm Only A File Sharing Bot!"
START_MSG = os.environ.get(
    "START_MESSAGE",
    "Hello {mention}\n\nI Can Store Private Files In A Specified Channel And Allow Others To Access Them Via A Special Link."
)

FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    f"Hello {{mention}}\n\n<b>You Must Join [This Channel](https://t.me/c/{FORCE_SUB_CHANNEL[4:]}) To Use Me.</b>\n\n"
    + "💡 *Also, consider joining these for extra content:*\n"
    + "\n".join([f"🔹 [Channel {i+1}](https://t.me/c/{ch[4:]})" for i, ch in enumerate(REQUESTED_JOIN_CHANNELS)])
)

# Logging Configuration
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
