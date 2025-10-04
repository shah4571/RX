# bot/handlers/__init__.py

from .start import register_start
from .cap import register_cap
from .account import register_account
from .withdraw import register_withdraw
from .support import register_support
from .admin import register_admin
from telegram.ext import Updater, CommandHandler

def init_handlers(updater: Updater):
    """
    Register all bot handlers to ensure the bot can handle commands.
    """
    dp = updater.dispatcher
    
    # Register the handlers
    dp.add_handler(CommandHandler("start", register_start))  # Registering /start command
    dp.add_handler(CommandHandler("cap", register_cap))      # Registering /cap command
    dp.add_handler(CommandHandler("account", register_account))  # Registering /account command
    dp.add_handler(CommandHandler("withdraw", register_withdraw))  # Registering /withdraw command
    dp.add_handler(CommandHandler("support", register_support))  # Registering /support command
    dp.add_handler(CommandHandler("admin", register_admin))  # Registering /admin command
