import asyncio

import aiosqlite

PATH = 'bot_organized.db'


async def create_users_table():
    async with aiosqlite.connect(PATH) as db:
        await db.execute('''
        CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL
        )''')
        await db.commit()


asyncio.run(create_users_table())
