# bot/handlers/start.py

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext

def register_start(update: Update, context: CallbackContext):
    """
    Handles the /start command and sends a welcome message with a menu button.
    """
    welcome_text = (
        "🎉 Welcome to Robot!\n\n"
        "Enter your phone number with the country code.\n"
        "Example: +91xxxxxxxxxx\n\n"
        "Type /cap to see available countries."
    )

    # Create a button for the hamburger (≡) menu
    menu_button = [
        [InlineKeyboardButton("≡ Menu", callback_data="menu_options")]  # Hamburger Menu
    ]

    # Create reply markup with the menu button
    reply_markup = InlineKeyboardMarkup(menu_button)

    # Send the message with the inline menu button
    update.message.reply_text(
        welcome_text,
        reply_markup=reply_markup
    )

def show_menu(update: Update, context: CallbackContext):
    """
    Shows the menu when the user clicks on the hamburger button (≡).
    """
    menu_options = [
        [InlineKeyboardButton("✅ Restart /start", callback_data="restart")],
        [InlineKeyboardButton("🌐 Capacity /cap", callback_data="capacity")],
        [InlineKeyboardButton("🎰 Check - Balance /account", callback_data="account")],
        [InlineKeyboardButton("💸 Withdraw Accounts /withdraw", callback_data="withdraw")],
        [InlineKeyboardButton("🆘 Need Help? /support", callback_data="support")]
    ]

    # Create reply markup for the options menu
    reply_markup = InlineKeyboardMarkup(menu_options)

    # Answer the callback query and update the message with the menu
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        "Please choose an option:",
        reply_markup=reply_markup
    )
