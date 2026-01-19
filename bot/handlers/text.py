from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def echo(message: Message):
    await message.answer(
        f"Ты написал: {message.text}"
    )

@router.message(lambda m: m.photo)
async def photo_handler(message: Message):
    await message.answer("Фото получено 📸")

