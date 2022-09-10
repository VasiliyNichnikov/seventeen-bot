from aiogram import types

from app import dp

from app.keyboards.services import services_keyboard
from app.keyboards.empty import empty_keyboard
from app.core.config import get_config


config = get_config()


@dp.message_handler(commands=[config.commands.start.name])
async def send_welcome(message: types.Message):
    global config
    await message.answer(text=config.commands.start.message, reply_markup=services_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    global config

    text = message.text

    for button in config.buttons.ready_buttons:
        if button.name == text:
            markup = services_keyboard if button.use_keyboard else empty_keyboard
            await message.answer(text=button.message, reply_markup=markup)
            return

    await message.answer(config.messages.error, reply_markup=services_keyboard)
