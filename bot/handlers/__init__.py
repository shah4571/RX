# Import all handler registration functions here

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
    
    # Register the handlers (removed group=0)
    dp.add_handler(CommandHandler("start", register_start))  # group=0 removed
    dp.add_handler(CommandHandler("cap", register_cap))
    dp.add_handler(CommandHandler("account", register_account))
    dp.add_handler(CommandHandler("withdraw", register_withdraw))
    dp.add_handler(CommandHandler("support", register_support))
    dp.add_handler(CommandHandler("admin", register_admin))

    # Register the callback query handler for menu options
    dp.add_handler(CallbackQueryHandler(show_menu, pattern="menu_options"))
