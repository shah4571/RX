from pyrogram import Client, filters
from pyrogram.types import Message
from .start import register_start
from .cap import register_cap
from .account import register_account
from .withdraw import register_withdraw
from .support import register_support
from .admin import register_admin

def init_handlers(app: Client):
    """
    Register all bot handlers
    """
    # Use lambda to correctly pass client and message parameters
    app.add_handler(filters.command("start")(lambda client, message: register_start(client, message)))
    app.add_handler(filters.command("cap")(lambda client, message: register_cap(client, message)))
    app.add_handler(filters.command("account")(lambda client, message: register_account(client, message)))
    app.add_handler(filters.command("withdraw")(lambda client, message: register_withdraw(client, message)))
    app.add_handler(filters.command("support")(lambda client, message: register_support(client, message)))
    app.add_handler(filters.command("admin")(lambda client, message: register_admin(client, message)))
