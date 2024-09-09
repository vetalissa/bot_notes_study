import asyncio
import logging
import sys

from handlers import cmd_start, menu_for_instruction
from loader import bot, dp


async def main() -> None:
    """
    Регистрация обработчиков команды /start и эха.
    Запуск процесса опроса для получения обновлений.
    """
    dp.message.register(cmd_start)
    dp.message.register(menu_for_instruction)

    await dp.start_polling(bot)


if __name__ == '__main__':
    """
    Настройка журналирования на уровне INFO.
    Запуск основной функции main с использованием asyncio.run().
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
