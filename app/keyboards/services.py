from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = KeyboardButton("Пример кнопки №1")
button2 = KeyboardButton("Пример кнопки №2")
button3 = KeyboardButton("Пример кнопки №3")

services_keyboard = ReplyKeyboardMarkup().row(button1, button2, button3)
