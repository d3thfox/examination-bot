from aiogram import Router,types
from aiogram.filters import Command
from bot_conf import bot

start_router = Router()
name = bot.get_me()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Здравствуйте - {message.from_user.first_name}\n"
                         f"У меня есть комманда для оставления жалобы /start_complaint")
