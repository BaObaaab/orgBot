from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon_ru import LEXICON_KEYBOARDS_RU
from keyboards.set_list_menu import set_list_buttons
from keyboards.menu_inline_keyboard import menu_keyboard

router: Router = Router()


@router.message(CommandStart())
async def process_command_start(message: Message):
    await message.answer(text=LEXICON_KEYBOARDS_RU['/start'], reply_markup=menu_keyboard)


@router.callback_query(Text(text='button_menu_was_pressed'))
async def process_pressed_menu(callback: CallbackQuery):
    await callback.message.edit_text(text='seome text', reply_markup=set_list_buttons.as_markup())


# @router.callback_query(Text(text=''))
