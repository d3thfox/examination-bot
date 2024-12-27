from aiogram import Router,types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(f"Здравствуйте{message.from_user.first_name}"
                         f"У меня есть комманда для осталения жалобы /start_complaint")
