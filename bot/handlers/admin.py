from telegram import Update
from telegram.ext import CallbackContext

def register_admin(update: Update, context: CallbackContext):
    # Temporary placeholder; implement later
    update.message.reply_text("Admin functionality is under development. Please check back later.")
