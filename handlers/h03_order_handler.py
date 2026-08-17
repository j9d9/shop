from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, ReplyKeyboardMarkup
from keyboards.reply import back_to_main_menu
from main import
router = Router()

@router.message(F.text == "buy")
async def show_main_menu(message: Message):
    """buying, order button"""
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="forming order:", reply_markup=back_to_main_menu)
    await message.answer(text='choose category', reply_markup=back_to_main_menu())


@router.message(F.text == "history")
async def make_history(message: Message):
    '''history'''
    chat_id = message.chat.id
    orders = db_get_last_orders(chat_id)

    if not orders:
        await message.answer(text="no orders")
        return

    text = 'your orders:\n\n'
    for order in orders:
        text += f'- {order.product_name}$ - {order.quantity} p\n'
    await message.answer(text=text)


@router.message(F.text == "Main menu🎞️")
async def handle_main_menu(message: Message, bot: Bot):

    '''getting main menu and deleting previous message'''

    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id -1)
    except  TelegramBadRequest:
        pass

    await show_main_menu(message)