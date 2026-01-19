from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.database import add_user
from bot.config import ADMIN_IDS

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    role = "admin" if message.from_user.id in ADMIN_IDS else "user"

    add_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        role=role
    )

    await message.answer(
        f"Привет 👋\nТвоя роль: {role}"
        "Это тестовый бот со всеми вариантами взаимодействия.\n"
        "Напиши /help"
    )

@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "/start — старт\n"
        "/help — помощь\n"
        "/buttons — кнопки\n"
        "/form — FSM форма"
    )
