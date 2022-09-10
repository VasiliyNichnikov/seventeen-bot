from aiogram import Bot, Dispatcher

from app.core.utils import get_telegram_token

telegram_token = get_telegram_token()
bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

# import commands
import app.commands
