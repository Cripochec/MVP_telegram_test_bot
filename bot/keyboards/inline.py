from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Нажми меня",
                callback_data="btn_click"
            )
        ]
    ]
)
