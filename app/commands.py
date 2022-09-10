from aiogram import types
from aiogram.types import InputFile

from app import dp
from app.core.config import get_config
from app.keyboards.empty import empty_keyboard
from app.core.utils import get_image_path
from app.keyboards.services import services_keyboard

config = get_config()


@dp.message_handler(commands=[config.commands.start.name])
async def send_welcome(message: types.Message):
    global config
    await message.answer(text=config.commands.start.message, reply_markup=services_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    global config

    bot = message.bot
    chat_id = message.chat.id
    text = message.text

    for button in config.buttons.ready_buttons:
        if button.name == text:
            markup = services_keyboard if button.use_keyboard else empty_keyboard
            has_image = button.image is not None
            btn_message = button.message
            if has_image is False:
                await message.answer(text=btn_message, reply_markup=markup)
            else:
                image_path = get_image_path(button.image)
                await bot.send_photo(chat_id, reply_markup=markup, photo=InputFile(image_path), caption=btn_message)
            return

    await message.answer(config.messages.error, reply_markup=services_keyboard)
