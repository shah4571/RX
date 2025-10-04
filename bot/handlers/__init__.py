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
    # Use Pyrogram's on_message decorator for command filters
    @app.on_message(filters.command("start"))
    async def start_handler(client: Client, message: Message):
        await register_start(client, message)

    @app.on_message(filters.command("cap"))
    async def cap_handler(client: Client, message: Message):
        await register_cap(client, message)

    @app.on_message(filters.command("account"))
    async def account_handler(client: Client, message: Message):
        await register_account(client, message)

    @app.on_message(filters.command("withdraw"))
    async def withdraw_handler(client: Client, message: Message):
        await register_withdraw(client, message)

    @app.on_message(filters.command("support"))
    async def support_handler(client: Client, message: Message):
        await register_support(client, message)

    @app.on_message(filters.command("admin"))
    async def admin_handler(client: Client, message: Message):
        await register_admin(client, message)
