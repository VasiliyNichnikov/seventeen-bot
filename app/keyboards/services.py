from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.core.config import get_config


config = get_config()

buttons = []

for info_btn in config.buttons.ready_buttons:
    button = KeyboardButton(info_btn.name)
    buttons.append(button)

services_keyboard = ReplyKeyboardMarkup().row(*buttons)
