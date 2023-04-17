from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, constants
from telegram.ext import ContextTypes
from typing import NoReturn, List
from random import shuffle

start_text: str = "*_Welcome to Classic Shoe Collections_*"
async def anytextInput(update: Update, context: ContextTypes.DEFAULT_TYPE) -> NoReturn:
    """sends introductory greetings and inline buttons of product listings"""
    
    keyboard: List[List[InlineKeyboardButton]]= [
        [InlineKeyboardButton("MEN Official Shoes \U0001F45E", callback_data="1")],
        [InlineKeyboardButton("MEN Outdoor footwear \U0001F45F", callback_data="2")],
        [InlineKeyboardButton("WOMEN Official Shoe\U0001F45E", callback_data="3")],
        [InlineKeyboardButton("WOMEN Outdoor footwear \U0001F97F", callback_data="4")],
        [InlineKeyboardButton("Contact Me \U0001F4DE", callback_data="5")]
    ]
    # shuffle(keyboard)
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(start_text, reply_markup=reply_keyboard, parse_mode=constants.ParseMode.MARKDOWN_V2)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    if query.data == "1":
        await MenShoes(update, context)
    elif query.data == "0": 
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Button not Implemented")  
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Button not Implemented, select *MEN Official shoes*", parse_mode=constants.ParseMode.MARKDOWN_V2)  

async def MenShoes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard: List[List[InlineKeyboardButton]]= [
        [InlineKeyboardButton("Add to Cart \U0001F6D2", callback_data="0")],
        [InlineKeyboardButton("Make purchase \U0001F6CD", callback_data="0")],
    ]
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    image1: str = "https://assets.adidas.com/images/w_600,f_auto,q_auto/75aee7eb0fc343d484c9adf30019d225_9366/Forum_Low_Shoes_White_GY8556_01_standard.jpg"
    image2: str = "https://www.u-buy.com.ng/productimg/?image=aHR0cHM6Ly9tLm1lZGlhLWFtYXpvbi5jb20vaW1hZ2VzL0kvNjEyNXlBZnNKS0wuX0FDX1VMMTE2MF8uanBn.jpg"
    image3: str = "https://rukminim1.flixcart.com/image/612/612/k4px6kw0/shoe/j/z/f/nc-aw19001tan-45-noble-curve-tan-original-imafnjhxkz3ygtzk.jpeg"
    await context.bot.send_photo(update.effective_chat.id, photo=image1, caption="ADDIDAS #15,OOO", reply_markup=reply_keyboard)
    await context.bot.send_photo(update.effective_chat.id, photo=image2, caption="NIKE #12,000", reply_markup=reply_keyboard)
    await context.bot.send_photo(update.effective_chat.id, photo=image3, caption="BROOKS #33,000", reply_markup=reply_keyboard)