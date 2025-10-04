import os
from pyrogram import Client, filters
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
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

    print("[INFO] Bot is starting...")

    # Start bot using Pyrogram
    app.run()

# Python-telegram-bot setup
def start_telegram(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is running!")

def main():
    # Start Python-telegram-bot
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_telegram))

    # Start the bot
    updater.start_polling()
    print("[INFO] Python-telegram-bot is running!")

    # Start Pyrogram bot concurrently
    start_pyrogram()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("[INFO] Bot stopped manually")
