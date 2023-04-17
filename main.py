import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger: logging.Logger = logging.getLogger(__name__)

if __name__ == '__main__':
    from telegrambot import handlerFuncs, BOT_TOKEN
    from telegram.ext import ApplicationBuilder, filters, CommandHandler, Application, MessageHandler, InlineQueryHandler, CallbackQueryHandler
    
    bot: Application = ApplicationBuilder().token(BOT_TOKEN).build()
    anytext_handler = MessageHandler(filters.TEXT, handlerFuncs.anytextInput)
    button_handler = CallbackQueryHandler(handlerFuncs.button)
    
    bot.add_handler(anytext_handler)
    bot.add_handler(button_handler)


    bot.run_polling()

    