import os
import asyncio
import threading
from pyrogram import Client
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from bot.config import BOT_TOKEN, API_ID, API_HASH
from bot.handlers import init_handlers

# Optional: পুরনো session ব্যাকআপ/মুছে ফেলা
SESSION_FILE = "RajuNewBot.session"
if os.path.exists(SESSION_FILE):
    os.rename(SESSION_FILE, SESSION_FILE + ".bak")  # ব্যাকআপ হিসেবে রাখবে

# Pyrogram Client setup
def start_pyrogram():
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

# Python-telegram-bot setup
async def start_telegram(update: Update, context: CallbackContext):
    await update.message.reply_text("Bot is running!")

async def main():
    # Start Python-telegram-bot
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the /start command handler for python-telegram-bot
    application.add_handler(CommandHandler("start", start_telegram))

    # Start Python-telegram-bot in an async loop
    application_task = asyncio.create_task(application.run_polling())
    print("[INFO] Python-telegram-bot is running!")

    # Wait until the polling task finishes
    await application_task

def start_both_bots():
    # Start the Pyrogram bot in a separate thread
    pyrogram_thread = threading.Thread(target=start_pyrogram)
    pyrogram_thread.start()

    # Run Python-telegram-bot with asyncio in the main thread
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

if __name__ == "__main__":
    try:
        start_both_bots()  # Start both bots in separate threads
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Bot stopped manually")
