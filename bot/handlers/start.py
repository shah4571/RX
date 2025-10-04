from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

def start(update: Update, context: CallbackContext):
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
    # Create the options menu to show after the (≡) button is clicked
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

def main():
    # Setup the Updater and Dispatcher
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    # Add handlers for /start and callback queries
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(show_menu, pattern="menu_options"))

    # Start polling
    updater.start_polling()

    print("[INFO] Bot is running!")

    updater.idle()

if __name__ == "__main__":
    main()
