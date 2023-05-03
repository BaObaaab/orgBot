from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, User

import aiosqlite

PATH = 'db.sqlite'


def keyboard():
    pass


async def add_data(message: Message):
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
            INSERT INTO other_menu(user_id, message_id)
            VALUES(?, ?);
        ''', (message.from_user.id, message.message_id)): ...
        await con.commit()


async def create_table():
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
            CREATE TABLE IF NOT EXISTS other_menu(
                user_id INTEGER NOT NULL,
                message_id INTEGER NOT NULL
            ); '''): ...
        await con.commit()


async def check_user(user: User) -> bool:
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
            SELECT user_id FROM other_menu
            WHERE user_id = ?;
        ''', (user.id,)) as cur:
            async for data in cur:
                if data:
                    return True
                return False


async def get_message_id(user: User) -> int:
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
            SELECT message_id FROM other_menu
            WHERE user_id = ?;
        ''', (user.id,)) as cur:
            async for data in cur:
                return data[0]


async def update_message_id(user: User, message_id):
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
            UPDATE other_menu
            SET message_id = ?
            WHERE user_id = ?;
        ''', (message_id, user.id)): ...
        await con.commit()


router = Router()


@router.startup()
async def a():
    print(2)
    await create_table()


@router.message(CommandStart())
async def command_start(message: Message, bot: Bot):
    msg = await message.answer(text='Текст', reply_markup=keyboard())
    user = message.from_user

    if not await check_user(user):
        return await add_data(message)

    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=await get_message_id(user)
    )
    await update_message_id(user, msg.message_id)
