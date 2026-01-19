import logging
from aiogram.types import Update

async def global_error_handler(update: Update, exception: Exception):
    logging.exception(
        f"Ошибка при обработке апдейта: {exception}"
    )
    return True
