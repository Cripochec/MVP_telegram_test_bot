from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📸 Отправить фото")],
        [KeyboardButton(text="ℹ️ Информация")]
    ],
    resize_keyboard=True
)
