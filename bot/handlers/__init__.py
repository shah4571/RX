# bot/handlers/__init__.py

from .start import register_start
from .cap import register_cap
from .account import register_account
from .withdraw import register_withdraw
from .support import register_support
from .admin import register_admin
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def init_handlers(updater: Updater):
    """
    Register all bot handlers
    """
    dp = updater.dispatcher
    
    # Register the handlers with the group=0 argument
    dp.add_handler(CommandHandler("start", register_start, group=0))  # Add group=0
    dp.add_handler(CommandHandler("cap", register_cap, group=0))
    dp.add_handler(CommandHandler("account", register_account, group=0))
    dp.add_handler(CommandHandler("withdraw", register_withdraw, group=0))
    dp.add_handler(CommandHandler("support", register_support, group=0))
    dp.add_handler(CommandHandler("admin", register_admin, group=0))

    # Register the callback query handler for menu options
    dp.add_handler(CallbackQueryHandler(show_menu, pattern="menu_options"))
