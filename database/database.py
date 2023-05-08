import aiosqlite
from aiogram.types import Message, User

PATH = 'bot_organized.db'


async def create_users_table():
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY UNIQUE,
        user_id INTEGER NOT NULL,
        user_name TEXT NOT NULL
        )'''): ...
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


async def add_users():
    async with aiosqlite.connect(PATH) as con:
        async with con.execute('''
        INSERT INTO users VALUES(user_id, user_name)'''): ...

