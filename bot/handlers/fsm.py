from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.states.form import UserForm

router = Router()

@router.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await message.answer("Как тебя зовут?")
    await state.set_state(UserForm.name)

@router.message(UserForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Сколько тебе лет?")
    await state.set_state(UserForm.age)

@router.message(UserForm.age)
async def get_age(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(
        f"Имя: {data['name']}\nВозраст: {message.text}"
    )
    await state.clear()
