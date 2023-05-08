from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon.lexicon_ru import BUTTONS

button_settings: InlineKeyboardButton = InlineKeyboardButton(text=BUTTONS['but_settings'],
                                                             callback_data='settings_button_was_pressed')
button_lists_of_task: InlineKeyboardButton = InlineKeyboardButton(text=BUTTONS['but_lists'],
                                                                  callback_data='button_of_list_was_pressed')
button_create_tasks: InlineKeyboardButton = InlineKeyboardButton(text=BUTTONS['but_create_task'],
                                                                 callback_data='button_create_task_was_pressed')

set_list_buttons: InlineKeyboardBuilder = InlineKeyboardBuilder()
set_list_buttons.row(button_create_tasks, button_lists_of_task, button_settings, width=1)
