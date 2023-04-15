from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from typing import NoReturn

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> NoReturn:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I am a bot")