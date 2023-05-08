import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import
from handlers import user_handlers, other_handlers
from keyboards.main_menu import set_main_menu

# Инициализация логгера
logger = logging.getLogger(__name__)


# Функция конфигурирования и записи бота
async def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')

    config:

    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Настройка меню бота
    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
