from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from bot.database import get_user_role

class RoleMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        user_id = None

        if isinstance(event, Message):
            user_id = event.from_user.id
        elif isinstance(event, CallbackQuery):
            user_id = event.from_user.id

        if user_id:
            role = get_user_role(user_id)
            data["role"] = role or "user"

        return await handler(event, data)
