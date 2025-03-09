import os
import logging
from logging.handlers import RotatingFileHandler

# ✅ Updated Bot Credentials
BOT_TOKEN = os.getenv("BOT_TOKEN", "7543846429:AAF5GDFBCDsM_tghg6g3MXnZW_Ol5Xx5Occ")
API_ID = int(os.getenv("API_ID", "979826"))
API_HASH = os.getenv("API_HASH", "238183386c30590d073b457166ba260d")

# ✅ Updated Owner & Database Credentials
OWNER_ID = int(os.getenv("OWNER_ID", "1074804932"))
DB_URL = os.getenv("DB_URL", "mongodb+srv://ygovcu:fY1f9Wovol3NqhUX@cluster0.1mdno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.getenv("DB_NAME", "Cluster0")

# ✅ Updated Channel & Subscription Settings
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1001847420676"))  # Log Channel
FORCE_SUB_CHANNEL = int(os.getenv("FORCE_SUB_CHANNEL", "-1002358532189"))  # Animes2u
FORCE_SUB_CHANNEL2 = int(os.getenv("FORCE_SUB_CHANNEL2", "0"))
FORCE_SUB_CHANNEL3 = int(os.getenv("FORCE_SUB_CHANNEL3", "0"))
FORCE_SUB_CHANNEL4 = int(os.getenv("FORCE_SUB_CHANNEL4", "0"))

# ✅ Other Bot Settings
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "900"))
PORT = int(os.getenv("PORT", "8080"))
TG_BOT_WORKERS = int(os.getenv("TG_BOT_WORKERS", "4"))

# ✅ Admin Handling
try:
    ADMINS = {OWNER_ID}  # Use a set to prevent duplicates
    ADMINS.update(map(int, os.getenv("ADMINS", str(OWNER_ID)).split()))
    ADMINS = list(ADMINS)  # Convert back to a list
except ValueError:
    raise Exception("⚠️ Your Admins list does not contain valid integers.")

# ✅ UI & Messaging Customization
CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION", "<b>@Animes2u - {file_name}</b>")
PROTECT_CONTENT = os.getenv('PROTECT_CONTENT', "True").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.getenv('DISABLE_CHANNEL_BUTTON', "True").lower() == "true"

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"
USER_REPLY_TEXT = "❌ Don't send me messages directly. I'm only a file-sharing bot!"

START_MSG = os.getenv("START_MESSAGE", "Hello {mention}\n\nI can store private files in a specified channel, and other users can access them via a special link.")
FORCE_MSG = os.getenv("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You need to join my channel/group to use me.\n\nPlease join the channel below:</b>")

# ✅ Logging Setup
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

# ✅ Logger Function
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
