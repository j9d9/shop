from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from database.utils import  db_get_all_category, db_get_finally_price

def create_categories_menu(chat_id):
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

def show_product_by_category(category_id):
    products = db_get_all_category(category_id)
    builder = InlineKeyboardBuilder()
    [builder.button(text=product.product_name, callback_data=f"product_{product.id}") for product in products]
    builder.adjust(3)
    builder.row(InlineKeyboardButton(text='back', callback_data = 'return_to category'))
    return builder.as_markup()

def quantity_cart_controls(quantity = 1):
    '''изм. кол-ва товаров в корзине'''
    builder = InlineKeyboardBuilder()
    builder.button(text = '➖', callback_data = 'action -')
    builder.button(text = str(quantity), callback_data = 'quantity')
    builder.button(text='➕', callback_data='action +')
    builder.button(text = 'в корзину', callback_data = 'положить в корзину')
    builder.button(text='🔙', callback_data='from_detail_to_category')
    builder.adjust(3, 1, 1)
    return builder.as_markup(resize_keyboard=True)



