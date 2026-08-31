from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, message_id, InlineKeyboardMarkup, chat_id_union

from keyboards.inline import show_product_by_category, create_categories_menu

router = Router()

@router.callback_query(F.data.regexp(r"^category_(\d+)$"))
async def show_product(query: CallbackQuery):
    '''показ всех продктов из конкретной категории'''
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    category_id = int(callback.data.split('_')[-1])

    try:
        await callback.bot.edit_message_text(
            text='pick products:',
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=show_product_by_category(category_id))
    except TelegramBadRequest:
        await callback.answer('category not found')

@router.callback_query(F.data=='return to category')
async def show_product_by_category(query: CallbackQuery):
    '''возврат к списку категорий'''
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id

    await callback.bot.edit_message_text(
        text='pick category:',
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=create_categories_menu()
    )


