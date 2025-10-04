from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from .start import register_start
from .cap import register_cap
from .account import register_account
from .withdraw import register_withdraw
from .support import register_support
from .admin import register_admin

# Register all bot handlers
def init_handlers(app: Client):
    """
    Register all bot handlers
    """
    # Directly pass the register_start function without using lambda
    app.add_handler(filters.command("start")(register_start))
    app.add_handler(filters.command("cap")(register_cap))
    app.add_handler(filters.command("account")(register_account))
    app.add_handler(filters.command("withdraw")(register_withdraw))
    app.add_handler(filters.command("support")(register_support))
    app.add_handler(filters.command("admin")(register_admin))
