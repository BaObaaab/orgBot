from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import BUTTONS

menu_button = InlineKeyboardButton = InlineKeyboardButton(text=BUTTONS['but_menu'],
                                                          callback_data='button_menu_was_pressed')
menu_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[[menu_button]])
