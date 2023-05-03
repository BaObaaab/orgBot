from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_KEYBOARDS_RU

# Инициализация роутера
router: Router = Router()


# Обрабочик для событий, которые неизветны боту
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_KEYBOARDS_RU['other_answer'])
