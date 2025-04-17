from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Karanor')],
        [KeyboardButton(text='Корзина')],
        [KeyboardButton(text='Контакты')],
        [KeyboardButton(text='0 нас')]
    ],
    resize_keyboard=True  # Это сделает кнопки подходящими по размеру
)
