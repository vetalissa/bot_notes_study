from aiogram import types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

from loader import dp


# Декоратор регистрирует этот обработчик для команды /start.
@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """
    Отправила ответное сообщение с приветствием, включая полное имя пользователя в жирном стиле.
    """
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!')


# Декоратор регистрирует этот обработчик для всех обычных сообщений.
@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
     Отправляет копию полученного сообщения в тот же чат.
     В случае ошибки типа TypeError, отправляется ответ 'Технические шоколадки!'.
    """
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Технические шоколадки!')
