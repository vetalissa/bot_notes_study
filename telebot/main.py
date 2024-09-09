import asyncio
import logging
import sys

from handlers import (buttons_for_choice, cmd_buttons_choice, cmd_start,
                      cmd_start_project, cmd_start_project2, cmd_test,
                      cms_buttons_choice2, menu_for_instruction)
from loader import bot, dp


async def main() -> None:
    """
    Регистрация обработчиков команды /start и эха.
    Запуск процесса опроса для получения обновлений.
    """
    dp.message.register(cmd_start)
    dp.message.register(menu_for_instruction)
    dp.message.register(cmd_test)
    dp.message.register(cmd_start_project)
    dp.message.register(cmd_buttons_choice)
    dp.message.register(cms_buttons_choice2)
    dp.message.register(buttons_for_choice)
    dp.message.register(cmd_start_project2)

    await dp.start_polling(bot)


if __name__ == '__main__':
    """
    Настройка журналирования на уровне INFO.
    Запуск основной функции main с использованием asyncio.run().
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
