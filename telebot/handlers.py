from contextlib import suppress

from aiogram import F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from loader import dp


#  '<blockquote>Цитата</blockquote>'
# '<b>(жирный)</b>'
#  '<i>курсив</i>'
#  '<u>подчеркивание</u>'
#  '''<pre><code class="language-python">
#     сюда пишем код
#  </code></pre>'''


# Декоратор регистрирует этот обработчик для команды /start.
@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Отправила ответное сообщение с приветствием, включая полное имя пользователя.
    """
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!')


@dp.message(Command('menu'))
async def menu_for_instruction(message: Message):
    """
    Меню-навигация
    """
    await message.answer('<b>Выбери что тебе нужно:</b> \n\n'
                         '<u>Start:</u>\n'
                         'Настраиваем проект /start_project1\n'
                         'Настраиваем проект /start_project2\n'
                         '\n'
                         '<u>Кнопки:</u>\n'
                         'Кнопки кликеры прям в контексте /inline_callback\n'
                         'Что бы делать вот такие команды /call_command\n'
                         'Кнопки с выбором вместо клавы /buttons_for_choice\n'
                         '\n\n\n'
                         '<u>Проектики мини:</u>\n'
                         
                         )


@dp.message(Command('start_project1'))
async def cmd_start_project(message: Message):
    await message.answer(
        ''' 
        начало...
        ✅ Создаем папку telegram_bot_project (имя может быть другим)
        ✅ Запускаем cmd и устанавливаем venv в эту папку
        ✅ Запускаем venv и устанавливаем:
                📥 pip install aiogram
                📥 pip install python-dotenv
        ✅ Создаем папку telebot(имя может быть другим)
        ✅ Создаем структуру проекта: 
            
            📁 telebot/
            |--📁 bot/
            |  |--📄 __init__.py 
            |  |--📄 bot.py 
            |  |
            |  |--📁 handlers/
            |  |  |--📄 __init__.py
            |  |  |--📄 text_handlers.py
            |  |  |--📄 photo_handlers.py
            |  |
            |  |--📁 tests/
            |     |--📄 __init__.py
            |     |--📄 test_handlers.py
            |     |--📄 test_business_logic.py
            |
            |--📁 config/ 
            |  |--📄 __init__.py 
            |  |--📄 config.py 
            |
            |--📁 media/ 
            |  |--📁 images/ 
            |  |--📁 documents/ 
            |
            |--📁 database/ 
            |  |--📄 __init__.py 
            |  |--📄 models.py 
            |
            |--📄 main.py 
            |--📄 .env 
            '''
    )


@dp.message(Command('start_project2'))
async def cmd_start_project2(message: Message):
    await message.answer("""
        ✅ Создаем бота в телеграмм и копируем токен;
        ✅ вставляем токен в 📄 .env:
            TOKEN=токен ваш
        ✅ достаем токен в 📄 config:
            <pre> <code class="language-python">
            import os
            from dotenv import load_dotenv
            load_dotenv()
            TOKEN = str(os.getenv('TOKEN'))
            </code></pre>
        ✅ подключаем отображение в 📄 loader:
           <pre> <code class="language-python">
            from aiogram import Bot, Dispatcher
            from aiogram.enums import ParseMode
            from aiogram.client.bot import DefaultBotProperties
            from config import TOKEN
            
            bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
            dp = Dispatcher()
            </code></pre>
        ✅  пишем отображение в 📄 main:  
            <pre> <code class="language-python">  
            import asyncio
            import logging
            import sys
            from handlers import функция_действия
            from loader import bot, dp
        
            async def main() -> None:
                dp.message.register(сюда пишем название функция_действия из handlers)
                await dp.start_polling(bot)
        
            if __name__ == '__main__':
                logging.basicConfig(level=logging.INFO, stream=sys.stdout)
                asyncio.run(main())
            </code></pre>
        """)


@dp.message(Command('call_command'))
async def cmd_inline_callable(message: Message):
    await message.answer(
        'Функция  выглядит так:\n\n'
        '''<pre> <code class="language-python">
        @dp.message(Command("имя_команды_для_вызова"))
        async def имя_функции_кнопки(message: types.Message):
            await message.answer(сюда пишем вывод что дает нажатие на кнопку)
        </code></pre>''')


@dp.message(Command('inline_callback'))
async def inline_callable(message: Message):
    await message.answer(
        f'Тело кнопки выглядит так:\n\n'

        '''<pre> <code class="language-python">
        @dp.message(Command('имя команды для вызова'))
        async def имя_функции_кнопки(message: types.Message):
            builder = InlineKeyboardBuilder()
            builder.add(types.InlineKeyboardButton(
            text='Текст на кнопке',
            callback_data='имя_ответа', ))
    
            with suppress(TelegramBadRequest):
                await message.answer(
                "текст над кнопкой",
                reply_markup=builder.as_markup())
        </code></pre>\n\n'''

        'Тело ответа выглядит так:\n\n'

        '''<pre> <code class="language-python">
        @dp.callback_query(F.data == 'имя ответа')
        async def имя_функции_ответа(callback: types.CallbackQuery):
            await callback.message.answer(вот сюда пишем, что вернется после нажатия на кнопку)
            await callback.answer() 
        </code></pre>'''
        'Пример: /test_inline_callback'
    )


@dp.message(Command("test_inline_callback"))
async def cmd_test(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Текст на кнопке",
        callback_data="test_answer", ))
    with suppress(TelegramBadRequest):
        await message.answer(
            "текст над кнопкой",
            reply_markup=builder.as_markup())


@dp.callback_query(F.data == "test_answer")
async def cmd_test_answer(callback: types.CallbackQuery):
    await callback.message.answer('Тут мы получаем какой-то ответ')
    await callback.answer()


button1 = KeyboardButton(text='Knopka 1')
button2 = KeyboardButton(text='Knopka 2')
keyboard = ReplyKeyboardMarkup(keyboard=[[button1, button2]],
                               resize_keyboard=True,
                               one_time_keyboard=True
                               )


@dp.message(Command("buttons_choice"))
async def cmd_buttons_choice(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=keyboard)


@dp.message(Command("buttons_choice2"))
async def cms_buttons_choice2(message: Message):
    kb = [[KeyboardButton(text='answer'),
           KeyboardButton(text='pupa')]]

    keyboard2 = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(text='this two variant for you, what you choice?',
                         reply_markup=keyboard2)


@dp.message(F.text == "answer")
async def process_answer_pipa(message: Message):
    await message.answer(
        text='Вот так выглядит ответ на нажатие на кнопку :\n\n'
             '''<pre> <code class="language-python">
             @dp.message(F.text == "текст кнопки")
             async def название_функции(message: Message):
                 await message.answer(
                     text="ответ который придет в сообщение",
                     reply_markup=types.ReplyKeyboardRemove())
             </code></pre>\n\n''',
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message(F.text == "pupa")
async def process_answer_pupa(message: Message):
    await message.answer(
        text='Да',
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message(Command('buttons_for_choice'))
async def buttons_for_choice(message: Message):
    await message.answer(
        'Функция кнопки выглядит так:\n\n'

        '''<pre> <code class="language-python">
    @dp.message(Command('команда_вызова_кнопок'))
    async def название_функции(message: Message):
        kb = [[KeyboardButton(text="текст на кнопке 1"),
               KeyboardButton(text="текст на кнопке 2")]]
 
        keyboard2 = ReplyKeyboardMarkup(
          keyboard=kb,
          resize_keyboard=True,
          one_time_keyboard=True
        )
        await message.answer(text="текст который выйдет перед кнопкой",
                            reply_markup=keyboard2)
        </code></pre>\n\n'''
        'пример: /buttons_choice  /buttons_choice2'
    )
