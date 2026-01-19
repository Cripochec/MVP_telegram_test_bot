from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.reply import main_reply_kb
from bot.keyboards.inline import inline_kb

router = Router()

@router.message(Command("buttons"))
async def buttons_cmd(message: Message):
    await message.answer(
        "Вот reply-кнопки:",
        reply_markup=main_reply_kb
    )
    await message.answer(
        "А вот inline-кнопка:",
        reply_markup=inline_kb
    )

@router.callback_query(lambda c: c.data == "btn_click")
async def inline_clicked(callback: CallbackQuery):
    await callback.answer("Кнопка нажата!")
    await callback.message.answer("Ты нажал inline-кнопку")
