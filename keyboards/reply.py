from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup


def start_keyboard():
    """starting the shop work"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='start')]
        ],
        resize_keyboard=True
    )

def phone_button():
    builder = ReplyKeyboardMarkup()
    builder.button(text="give your phone to integrate", request_contact=True)
    return builder(resize_keyboard=True)

def get_main_menu():
    """creating main menu service"""
    builder = ReplyKeyboardBuilder()
    builder.button(text="Buy💸")
    builder.button(text="History🕓")
    builder.button(text="Order🧺")
    builder.button(text="Settings⚙️")
    builder.adjust(1, 1, 1, 1)
    return builder.as_markup(resize_keyboard=True)

def back_to_main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="main menu")
    return builder.as_markup(resize_keyboard=True)