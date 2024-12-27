from tkinter.font import names

from aiogram import Router, types,F
from aiogram.filters import Command
from aiogram.fsm.state import State,StatesGroup
from aiogram.fsm.context import FSMContext
from bot_conf import database

complaint_router = Router()

class ComplaintDialog(StatesGroup):
    name = State()
    contact = State()
    complaint = State()

@complaint_router.message(Command('start_complaint'))
async def start_complaint(message: types.Message , state: FSMContext):
    await message.answer('Введите ваше имя')
    await state.set_state(ComplaintDialog.name)

@complaint_router.message(ComplaintDialog.name)
async def start_complaint(message: types.Message , state: FSMContext):
    name = message.text
    if message.isdigit():
        await message.answer('Можно писать только буквами')
        return
    await state.update_data(name=name)
    await message.answer(f"Введите ваш номер телефона\n"
                         f"Вводите номер с регионом\n"
                         f"Пример: 996111222333")
    await state.set_state(ComplaintDialog.contact)

@complaint_router.message(ComplaintDialog.contact)
async def start_complaint(message: types.Message , state: FSMContext):
    contact = message.text
    if not contact.isdigit():
        await message.answer("Пишите цифрами")
        return
    if len(contact) > 12:
        await message.answer('Вы не можете превышать 12 символов')
        return
    await state.update_data(contact=contact)
    await message.answer("Можете написать жалобу")
    await state.set_state(ComplaintDialog.complaint)

@complaint_router.message(ComplaintDialog.complaint)
async def start_complaint(message: types.Message , state: FSMContext):
    await state.update_data(complaint=message.text)
    await message.answer("Ваша жалоба принята")
    data = await state.get_data()
    database.insert_complaint(data)
    await message.answer(f'Ваше имя: {data["name"]}\n'
                         f'Ваша жалоба: {data["complaint"]}')

    await state.clear()










