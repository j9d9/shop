from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup

from keyboards.reply import back_to_main_menu
from main import bot

router = Router()

@router.message(F.text == "buy")
async def show_main_menu(message: Message):
    """buying, order button"""
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="choise", reply_markup=back_to_main_menu)