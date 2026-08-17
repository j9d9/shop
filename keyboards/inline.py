from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import  db_get_all_category, db_get_finally_price

def create_categories_menu(chat_id)
    '''cateories menu'''
    categories = db_get_all_category()
    total_price = db_get_finally_price(chat_id)

    builder = InlineKeyboardBuilder()
    builder.button(text=f"order ({total_price if total_price else 0}$)",
                  callback_data="order",
                  )
    [builder.button(text=category.category_name, callback_data=f"category_{category.category.id}") for category in categories]

    builder.adjust(1, 2)
    return builder.as_markup()
