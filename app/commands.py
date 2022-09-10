from aiogram import types

from app import dp

from app.keyboards.services import services_keyboard
from app.keyboards.empty import empty_keyboard


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(text="Привет это сообщение приветсвия!", reply_markup=services_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    match message.text:
        case "Пример кнопки №1":
            await message.answer(text="Информация о кнопке №1", reply_markup=empty_keyboard)

        case "Пример кнопки №2":
            await message.answer(text="Информация о кнопке №2", reply_markup=empty_keyboard)

        case "Пример кнопки №3":
            await message.answer("Информация о кнопке №3", reply_markup=empty_keyboard)

        case _:
            await message.answer("Сообщение об ошибке", reply_markup=services_keyboard)

