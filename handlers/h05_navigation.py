from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message


router = Router()

@router.message(F.text= 'back')
async def return_to_category_menu(message: Message, bot: Bot):
    try
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    except TelegramBadRequest:
        pass
    await make_order(message, bot)
