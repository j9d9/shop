from aiogram import Router, F
from aiogram.types import Message
from database.utils import db_update_user, db_create_user_cart
from keyboards.reply import get_main_menu

router = Router()

@router.message(F.contact)
async def update_contact(message: Message):
    """updating user contact, getting phone number"""
    chat_id = message.chat.id
    phone = message.contact.phone_number

    db_update_user(chat_id, phone)



    if db_create_user_cart(chat_id):
        await message.answer(text="registration successful")
    await show_main_menu(message)


async def show_main_menu(message: Message):
    """show main menu"""
    await message.answer(text="choise", reply_markup=get_main_menu())
