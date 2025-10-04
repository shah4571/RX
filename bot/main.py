import os
import asyncio
import threading
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import init_handlers

# Optional: পুরনো session ব্যাকআপ/মুছে ফেলা
SESSION_FILE = "RajuNewBot.session"
if os.path.exists(SESSION_FILE):
    os.rename(SESSION_FILE, SESSION_FILE + ".bak")  # ব্যাকআপ হিসেবে রাখবে

# Pyrogram Client setup (aiohttp বাদ দিয়ে)
def start_pyrogram():
    # এখানে asyncio ইভেন্ট লুপ তৈরি করা হচ্ছে
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)  # থ্রেডের জন্য লুপ সেট করতে হবে

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
    app.run()

# বট চালানোর জন্য থ্রেডিং পদ্ধতি
def start_both_bots():
    # Pyrogram বট চালানো হবে
    pyrogram_thread = threading.Thread(target=start_pyrogram)
    pyrogram_thread.start()

if __name__ == "__main__":
    try:
        start_both_bots()  # শুধু Pyrogram বট চালানো হবে
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Bot stopped manually")
