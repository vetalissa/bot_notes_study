import random
from contextlib import suppress

from aiogram import F, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command, CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, KeyboardButton, Message,
                           ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from loader import dp

kb = [[KeyboardButton(text='menu')]]
keyboard2 = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
)

jokes: dict[int, str] = {
    1: 'с хабра, описание фильмов Матрица\n\nСудя по всему, в городе машин либо очень либеральный мэр, либо очень криворукие сисадмины. Иначе как объяснить, что свободные люди беспрепятственно подключаются к вражеской ИТ-системе? Причем удаленно из тарантаса, летающего по канализации! Т.е. мало того, что у машин в сточных трубах развернут высокоскоростной Wi-Fi, так они еще и пускают в свою сеть всех подряд, позволяя неавторизованным пользователям получать данные из системы, вносить в нее изменения и общаться между собой. Красота!',
    2: '- У меня на одном курсе был фин, он приехал к нам т.к. был очарован культурой гопников. Он хотел проникнуться ею у первоисточника и подтянуть мат. И вот где-то в Питере он припал к истокам, все-все выучил и загорелся желанием принести культуру другим иностранцам группы. А там были бразильцы, немцы итальянцы, французы и китаец. И вот захожу как-то я в группу и там хором повторяют слова "ъуъ" и "съка" с шестью разными акцентами.\n- Хотелось бы послушать, как они говорили "ъуъ"',
    3: 'Я в восторге от наших учителей.\nСыну в школе дали домашнее задание, где, среди прочего, был вопрос "как связаны буква А4 и бык?"\nРассказал ему про финикийский алфавит, как первую фонетическую письменность. Что там была буква "алеф", очень похожая на нашу современную "А", и что слово "алеф" означало "бык". Что, возможно, букву так назвали, потому что если развернуть ее, то она похожа на морду быка с рогами.\nЕще очень радовался, что детям во втором классе такие вещи рассказывают.\nУчительница поставила ребенку двойку, заявив, что он фантазировал в домашнем задании. А правильный ответ: если к слову "бык" добавить "а", получится родительный падеж.\nЯ не планировал в таком раннем возрасте рассказывать сыну, что половина окружающих людей - идиоты, но, видимо, придется :-)',
    4: 'у меня на балконе сосулька растет метровая, прямо над машиной, которая ссигналит каждую ночь. Я эту сосульку из распылителя подкармливаю.',
    5: 'xx: Мне сейчас спам пришел "Я живу в доме напротив, вот моя ссылка *адрес ссылки*. Давай познакомимся". Я ответил, что живу напротив морга и меня пугают такие знакомства',
    6: 'xxx: В командировке на съемной квартире нужна была марля, чтобы погладить футболку. Начал шариться по всем ящикам. Марлю не нашел, зато нашел ключ в шкафу между простынями. Вспомнил, что один ящик в этом шкафу был заперт. Попробовал открыть его найденным ключом. Открыл. Внутри нашел марлю. Не зря в квесты играл..'
}


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f'Привет, {hbold(message.from_user.full_name)}!')


@dp.message(Command('start_project1'))
async def cmd_start_project(message: Message):
    await message.answer(
        ''' начало...
        ✅ Создаем папку telegram_bot_project (имя может быть другим)
        ✅ Запускаем cmd и устанавливаем venv в эту папку
        ✅ Запускаем venv и устанавливаем:
                📥 pip install aiogram
                📥 pip install python-dotenv
        ✅ Создаем папку telebot(имя может быть другим)
        ✅ Создаем структуру проекта:
        \n
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
    ''')


@dp.message(Command('start_project2'))
async def cmd_start_project2(message: Message):
    await message.answer("""
        ✅ Создаем бота в телеграмм и копируем токен;
        ✅ вставляем токен в 📄 .env:
            TOKEN=токен ваш
        ✅ достаем токен в 📄 config:
            <pre> <code class='language-python'>
            import os
            from dotenv import load_dotenv
            load_dotenv()
            TOKEN = str(os.getenv('TOKEN'))
            </code></pre>
        ✅ подключаем отображение в 📄 loader:
           <pre> <code class='language-python'>
            from aiogram import Bot, Dispatcher
            from aiogram.enums import ParseMode
            from aiogram.client.bot import DefaultBotProperties
            from config import TOKEN\n
            bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
            dp = Dispatcher()
            </code></pre>\
        ✅  пишем отображение в 📄 main:
            <pre> <code class='language-python'>
            import asyncio
            import logging
            import sys
            from handlers import функция_действия
            from loader import bot, dp\n
            async def main() -> None:
                dp.message.register(сюда пишем название функция_действия из handlers)
                await dp.start_polling(bot)
            \n
            if __name__ == '__main__':
                logging.basicConfig(level=logging.INFO, stream=sys.stdout)
                asyncio.run(main())
            </code></pre>
        """)


@dp.message(Command('call_command'))
async def cmd_inline_callable(message: Message):
    await message.answer(
        'Функция  выглядит так:\n\n'
        '''<pre> <code class='language-python'>
        @dp.message(Command('имя_команды_для_вызова'))
        async def имя_функции_кнопки(message: types.Message):
            await message.answer(сюда пишем вывод что дает нажатие на кнопку)
        </code></pre>''')


@dp.message(Command('inline_button'))
async def inline_button(message: Message):
    await message.answer(
        'Функция кнопки выглядит так:\n\n'

        '''<pre> <code class='language-python'>
        @dp.message(Command('имя команды для вызова'))
        async def имя_функции_кнопки(message: types.Message):
            builder = InlineKeyboardBuilder()
            builder.add(types.InlineKeyboardButton(
            text='Текст на кнопке',
            callback_data='имя_ответа', # если нужен ответ после нажатия на кнопку
            url='ссылка, если вам нужно чтобы кнопка пере отправляла куда-то'))\n
            with suppress(TelegramBadRequest):
                await message.answer(
                'текст над кнопкой',
                reply_markup=builder.as_markup())
        </code></pre>\n\n'''

        'Функция ответа выглядит так:\n\n'

        '''<pre> <code class='language-python'>
        @dp.callback_query(F.data == 'имя ответа')
        async def имя_функции_ответа(callback: types.CallbackQuery):
            await callback.message.answer(вот сюда пишем, что вернется после нажатия на кнопку)
            await callback.answer()
        </code></pre>'''
        'Пример: /test_inline_callback'
    )


@dp.message(Command('test_inline_callback'))
async def cmd_test(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text='Текст на кнопке',
        callback_data='test_answer', ))
    with suppress(TelegramBadRequest):
        await message.answer(
            'текст над кнопкой',
            reply_markup=builder.as_markup())


@dp.callback_query(F.data == 'test_answer')
async def cmd_test_answer(callback: types.CallbackQuery):
    await callback.message.answer('Тут мы получаем какой-то ответ')
    await callback.answer()


button1 = KeyboardButton(text='Knopka 1')
button2 = KeyboardButton(text='Knopka 2')
keyboard = ReplyKeyboardMarkup(keyboard=[[button1, button2]],
                               resize_keyboard=True,
                               one_time_keyboard=True
                               )


@dp.message(Command('buttons_choice'))
async def cmd_buttons_choice(message: Message):
    await message.answer(text='Чего кошки боятся больше?',
                         reply_markup=keyboard)


@dp.message(Command('buttons_choice2'))
async def cms_buttons_choice2(message: Message):
    kb = [[KeyboardButton(text='answer'),
           KeyboardButton(text='pupa')]]

    keyboard3 = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.answer(text='this two variant for you, what you choice?',
                         reply_markup=keyboard3)


@dp.message(F.text == 'answer')
async def process_answer_pipa(message: Message):
    await message.answer(
        text='Вот так выглядит ответ на нажатие на кнопку :\n\n'
             '''<pre> <code class='language-python'>
             @dp.message(F.text == 'текст кнопки')
             async def название_функции(message: Message):
                 await message.answer(
                     text='ответ который придет в сообщение',
                     reply_markup=types.ReplyKeyboardRemove())
             </code></pre>\n\n''',
        reply_markup=keyboard2
    )


@dp.message(F.text == 'pupa')
async def process_answer_pupa(message: Message):
    await message.answer(
        text='Да',
        reply_markup=keyboard2
    )


@dp.message(Command('buttons_for_choice'))
async def buttons_for_choice(message: Message):
    await message.answer(
        'Функция кнопки выглядит так:\n\n'

        '''<pre> <code class='language-python'>
    @dp.message(Command('команда_вызова_кнопок'))
    async def название_функции(message: Message):
        kb = [[KeyboardButton(text='текст на кнопке 1'),\nKeyboardButton(text='текст на кнопке 2')]]
        keyboard2 = ReplyKeyboardMarkup(
          keyboard=kb,
          one_time_keyboard=True, # после нажатия кнопки свернутся
          resize_keyboard=True # эта штука сделает их меньше
          input_field_placeholder='этот текст будет виден в поле ввода'
        )
        await message.answer(text='текст который выйдет перед кнопкой',
                            reply_markup=keyboard2)
        </code></pre>\n\n'''
        'пример: /buttons_choice  /buttons_choice2\n\n'
        'Специальные кнопки с автоматическим действием /special_buttons'
    )


@dp.message(Command('special_buttons'))
async def buttonss_special_move(message: Message):
    await message.answer(
        'Функция кнопки выглядит так:\n\n'

        '''<pre> <code class='language-python'>
            # Инициализируем билдер
            kb_builder = ReplyKeyboardBuilder()

            # Создаем кнопки
            contact_btn = KeyboardButton(
                text='Отправить телефон',
                request_contact=True
            )
            geo_btn = KeyboardButton(
                text='Отправить геолокацию',
                request_location=True
            )
            poll_btn = KeyboardButton(
                text='Создать опрос/викторину',
                request_poll=KeyboardButtonPollType()
            )

            # Добавляем кнопки в билдер
            kb_builder.row(contact_btn, geo_btn, poll_btn, width=1)

            # Создаем объект клавиатуры
            keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
                resize_keyboard=True,
                one_time_keyboard=True
            )
        </code></pre>\n\n'''
    )


@dp.message(Command('gif_or_image'))
async def send_media_file(message: Message):
    await message.answer(
        'Функция кнопки выглядит так:\n\n'

        '''<pre> <code class='language-python'>
        @dp.message()
        async def название_функции(message: types.Message) -> None:
        try:
            if PARAMETER_SENDER == 'Гифку':
                API_GIF_URL = 'ссылка на объект'
                gif_response = requests.get(API_GIF_URL)
                if gif_response.status_code == 200:
                    gif_link = gif_response.json()['image'] #тут мы достаем из json так как вым нужно
                    await message.bot(SendVideo(chat_id=message.chat.id, video=gif_link))
            elif PARAMETER_SENDER == 'Картинку':
                API_IMAGE_URL = 'ссылка на объект'
                image_response = requests.get(API_IMAGE_URL)
                if image_response.status_code == 200:
                    cat_link = image_response.json()[0]['url'] #тут мы достаем из json так как вым нужно
                    await message.bot(SendPhoto(chat_id=message.chat.id, photo=cat_link))

        except TypeError:
            await message.answer('Технические шоколадки!')
        </code></pre>\n\n'''
    )


@dp.message(Command('filter_text'))
async def filter_text(message: Message):
    await message.answer(
        'Декоратор пишем так, если хотим что бы наша функция'
        'отрабатывала на какие-то определенные значения в тексте;'
        'и соблюдаем порядок таких функций:\n\n'
        '''<pre> <code class='language-python'>
        # Этот хэндлер будет срабатывать на тип контента "photo"
        @dp.message(F.photo)
        # Этот хэндлер проверяет, что у нас поступило число и оно равно 1
        @dp.message(lambda x: x.text and x.text.isdigit() and 1 = int(x.text))
        # Этот хэндлер проверяет что поступил текст, который есть в списке
        @dp.message(F.text.lower().in_(['а вот сюда пишем текст на который откликается']))
        # Этот хэндлер будет срабатывать на тип контента "voice", "video" или "text"
        @dp.message(F.content_type.in_({'voice', 'video', 'text'}))
        </code></pre>''')


@dp.message(Command('mach_buttons_num'))
async def filter_text(message: Message):
    await message.answer(
        'Функция для написания клавиатуры с большим количеством выбора кнопок с цифрами\n\n'
        '''<pre> <code class='language-python'>
        num_ls = [] #пустой список для генерации
        num_buttons = [] #список кнопок

        #создаем список кнопок от 1 до 99
        for i in range(1, 100):
            num_ls.append(KeyboardButton(text=str(i)))
            #количество кнопок в строке будет 9
            if not i % 9:
                num_buttons.append(num_ls)
                num_ls = []
        #дополнительно добавляем еще кнопку 100
        num_buttons.append([KeyboardButton(text='100')])
        num_keyboard = ReplyKeyboardMarkup(
                    keyboard=num_buttons,
                    resize_keyboard=True)
        </code></pre>''')


@dp.message(Command('format_text'))
async def format_text(message: Message):
    await message.answer(
        'Выбери что хочешь посмотреть:\n\n'
        '/html - пример разметки с помощью HTML\n'
        '/markdownv2 - пример разметки с помощью MarkdownV2\n'
        '/noformat - пример с разметкой, но без указания параметра parse_mode')


@dp.message(Command('html'))
async def format_text_html(message: Message):
    await message.answer(
        'как работает HTML-разметка:\n\n'
        '<b>Это жирный текст</b>   b\n'
        '<i>Это наклонный текст</i>  i\n'
        '<u>Это подчеркнутый текст</u>  u\n'
        '<span class="tg-spoiler">А это спойлер</span>   span class=tg-spoiler"\n\n'
        'Другие варианты: /markdownv2 /noformat')


@dp.message(Command('MarkdownV2'))
async def format_text_markdownV2(message: Message):
    await message.answer(
        'как работает MarkdownV2\-разметка:\n\n'
        '*Это жирный текст*\n'
        '_Это наклонный текст_\n'
        '__Это подчеркнутый текст__\n'
        '||А это спойлер||\n\n'
        '''<pre> <code class='language-python'>
        #'*Это жирный текст*'
        #'_Это наклонный текст_'
        #'__Это подчеркнутый текст__'
        #'||А это спойлер||'
       </code></pre>'''
        'Другие варианты: /html /noformat')


@dp.message(Command('noformat'))
async def format_text_noformat(message: Message):
    await message.answer(
        'как отображается текст, если не указать '
        'параметр parse_mode:\n\n'
        '<b>Это мог бы быть жирный текст</b>\n'
        '_Это мог бы быть наклонный текст_\n'
        '<u>Это мог бы быть подчеркнутый текст</u>\n'
        '||А это мог бы быть спойлер||\n\n'
        '''<pre> <code class='language-python'>
       #'<b>Это мог бы быть жирный текст</b> b b'
        #'_Это мог бы быть наклонный текст_'
        #'<u>Это мог бы быть подчеркнутый текст</u> u u'
        #'||А это мог бы быть спойлер'
       </code></pre>'''
        'Другие варианты: /html /markdownv2')


@dp.message(Command('change_message'))
async def change_message(message: Message):
    keyboard = [
        [InlineKeyboardButton(text='Способ 1 генерацией другого ответа от кнопки', callback_data='change_message1')],
        [InlineKeyboardButton(text='Способ 2 с удалением сообщения', callback_data='change_message2')],
        [InlineKeyboardButton(text='Способ 3 с редактированием сообщения', callback_data='change_message3')],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    await message.answer(
        'Есть несколько вариантов изменения сообщения:\n\n'
        'Способ 1. Отправка нового сообщения без удаления старого\n'
        '''<pre> <code class='language-python'>
       @dp.callback_query(F.data == 'название_ответа')
       async def process_more_press(callback: CallbackQuery):
           keyboard = [[InlineKeyboardButton(text='Текст инлайн кнопки', callback_data='название_ответа')]]
           markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
           # Отвечаем на callback, чтобы убрать часики
           await callback.answer()
           # Отправляем в чат новое сообщение с шуткой
           await callback.message.answer(
               text=Словарь_с_возможными_оттветами[random.randint(1, len(jokes))],
               reply_markup=markup
           )
       </code></pre>'''
        'Способ 2. Отправка нового сообщения с удалением старого'
        '''<pre> <code class='language-python'>
        @dp.callback_query(F.data == 'название_ответа')
        async def process_more_press(callback: CallbackQuery):
            keyboard = [[InlineKeyboardButton(text='Текст инлайн кнопки', callback_data='название_ответа')]]
            markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
            # Удаляем сообщение, в котором была нажата кнопка
            await callback.message.delete()
            # Отправляем в чат новое сообщение с шуткой
            await callback.message.answer(
                text=Словарь_с_возможными_оттветами[random.randint(1, len(jokes))],
                reply_markup=markup
            )
        </code></pre>'''
        'Способ 3. Редактирование сообщения'
        '''<pre> <code class='language-python'>
        @dp.callback_query(F.data == 'название_ответа')
        async def process_more_press(callback: CallbackQuery):
            keyboard: = [[InlineKeyboardButton(text='Текст инлайн кнопки', callback_data='название_ответа')]]
            markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
            # Редактируем сообщение
            await callback.message.edit_text(
                text=Словарь_с_возможными_оттветами[random.randint(1, len(jokes))],
                reply_markup=markup
)
        </code></pre>'''
        'Другие варианты: /html /markdownv2',
        reply_markup=markup)


@dp.callback_query(F.data == 'change_message1')
async def change_message1(callback: CallbackQuery):
    keyboard = [
        [InlineKeyboardButton(text='Способ 1 генерацией другого ответа от кнопки', callback_data='change_message1')],
        [InlineKeyboardButton(text='Способ 2 с удалением сообщения', callback_data='change_message2')],
        [InlineKeyboardButton(text='Способ 3 с редактированием сообщения', callback_data='change_message3')],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Отвечаем на callback, чтобы убрать часики
    await callback.answer()
    # Отправляем в чат новое сообщение с шуткой
    await callback.message.answer(
        text=jokes[random.randint(1, len(jokes))],
        reply_markup=markup
    )


@dp.callback_query(F.data == 'change_message2')
async def change_message2(callback: CallbackQuery):
    keyboard = [
        [InlineKeyboardButton(text='Способ 1 генерацией другого ответа от кнопки', callback_data='change_message1')],
        [InlineKeyboardButton(text='Способ 2 с удалением сообщения', callback_data='change_message2')],
        [InlineKeyboardButton(text='Способ 3 с редактированием сообщения', callback_data='change_message3')],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Удаляем сообщение, в котором была нажата кнопка
    await callback.message.delete()
    # Отправляем в чат новое сообщение с шуткой
    await callback.message.answer(
        text=jokes[random.randint(1, len(jokes))],
        reply_markup=markup
    )


@dp.callback_query(F.data == 'change_message3')
async def process_more_press(callback: CallbackQuery):
    keyboard = [
        [InlineKeyboardButton(text='Способ 1 генерацией другого ответа от кнопки', callback_data='change_message1')],
        [InlineKeyboardButton(text='Способ 2 с удалением сообщения', callback_data='change_message2')],
        [InlineKeyboardButton(text='Способ 3 с редактированием сообщения', callback_data='change_message3')],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    # Редактируем сообщение
    await callback.message.edit_text(
        text=jokes[random.randint(1, len(jokes))],
        reply_markup=markup
    )


@dp.message()
async def buttons_for_menu(message: Message):
    await message.answer(text='меню''<b>Выбери что тебе нужно:</b> \n\n'
                              '<u>Start:</u>\n'
                              'Настраиваем проект /start_project1\n'
                              'Настраиваем проект /start_project2\n'
                              '\n'
                              '<u>Кнопки:</u>\n'
                              'Кнопки кликеры прям в контексте /inline_button\n'
                              'Что бы делать вот такие команды /call_command\n'
                              'Кнопки с выбором вместо клавы /buttons_for_choice\n'
                              'Кнопки с большим выбором (чисел) /mach_buttons_num\n'
                              'Как вставить картинку или гифку через url /gif_or_image\n'
                              'запуск функции по слову /filter_text\n'
                              'Форматирование текста /format_text\n'
                              'Изменение сообщения /change_message\n'
                              '\n\n\n'
                              '<u>Проектики мини:</u>\n',
                         reply_markup=keyboard2)
