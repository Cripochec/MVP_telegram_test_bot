from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.database import get_user_role

router = Router()

@router.message(Command("admin"))
async def admin_cmd(message: Message):
    role = get_user_role(message.from_user.id)

    if role != "admin":
        await message.answer("⛔ У тебя нет доступа")
        return

    await message.answer("👮 Админ-панель (заглушка)")

@router.message(Command("cool"))
async def cool_cmd(message: Message, role: str):
    if role != "admin":
        await message.answer("⛔ Эта команда только для админа")
        return

    await message.answer(
        "😎 Ты реально крут.\n"
        "Продакшн одобряет тебя."
    )