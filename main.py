from telegrambot import BOT_TOKEN, start
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, Application

if __name__ == '__main__':
    bot: Application = ApplicationBuilder().token(BOT_TOKEN).build()
    start_handler = CommandHandler('start', start)
    bot.add_handler(start_handler)

    bot.run_polling()

    