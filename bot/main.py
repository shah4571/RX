import os
import asyncio
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import init_handlers

# Optional: পুরনো session ব্যাকআপ/মুছে ফেলা
SESSION_FILE = "RajuNewBot.session"
if os.path.exists(SESSION_FILE):
    os.rename(SESSION_FILE, SESSION_FILE + ".bak")  # ব্যাকআপ হিসেবে রাখবে

# Pyrogram Client setup (aiohttp বাদ দিয়ে)
async def start_pyrogram():
    # এখানে asyncio ইভেন্ট লুপ তৈরি করা হচ্ছে
    app = Client(
        "RajuNewBot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        parse_mode="html",
        ipv6=False
    )

    # Register all handlers
    init_handlers(app)

    print("[INFO] Pyrogram bot is starting...")

    # Start bot using Pyrogram
    await app.start()

if __name__ == "__main__":
    try:
        # Directly run the asyncio loop
        asyncio.run(start_pyrogram())  # Using asyncio to run the bot
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Bot stopped manually")
