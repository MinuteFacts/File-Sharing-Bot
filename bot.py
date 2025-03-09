import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from aiohttp import web
from pyrogram import Client
from pyrogram.enums import ParseMode
import pyrogram.utils
from plugins import web_server
from config import API_HASH, API_ID, LOGGER, BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, CHANNEL_ID, PORT

# Set Minimum Channel ID
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

# Logging Setup
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

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.username = usr_bot_me.username
        self.invitelinks = {}

        # Force Subscription Handling (Optimized)
        force_sub_channels = {
            1: FORCE_SUB_CHANNEL,
            2: FORCE_SUB_CHANNEL2,
            3: FORCE_SUB_CHANNEL3,
            4: FORCE_SUB_CHANNEL4
        }

        for i, channel in force_sub_channels.items():
            if channel and channel != 0:
                try:
                    chat = await self.get_chat(channel)
                    link = chat.invite_link or await self.export_chat_invite_link(channel)
                    self.invitelinks[f"invitelink{i}"] = link
                except Exception as e:
                    self.LOGGER(__name__).warning(f"Error with FORCE_SUB_CHANNEL{i}: {e}")
                    self.LOGGER(__name__).warning(f"Make sure the bot is an admin in channel {channel} with 'Invite Users via Link' permission.")
                    sys.exit()

        # Database Channel Check
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Hey 🖐")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).error(f"Bot lacks permission in the DB Channel: {e}")
            self.LOGGER(__name__).error(f"Ensure the bot is an admin in {CHANNEL_ID} with 'Send Messages' permission.")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"✅ Bot Running as @{self.username}!\nCreated By: https://t.me/Animes2u")

        # Web Server Response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("❌ Bot Stopped...")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
