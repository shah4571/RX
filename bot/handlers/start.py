from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def register_start(client: Client, message: Message):
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
    await message.reply(
        welcome_text,
        reply_markup=reply_markup
    )

async def show_menu(client: Client, message: Message):
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
    query = message.callback_query
    await query.answer()
    await query.edit_message_text(
        "Please choose an option:",
        reply_markup=reply_markup
    )
