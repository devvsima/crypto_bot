from aiogram.types import (
    ReplyKeyboardRemove,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


async def base_kb():
    kb = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="⭐️ Favorites"),
            ],
            [
                KeyboardButton(text="📔 About coins"),
            ],
            [
                KeyboardButton(text="⚙️ Settings"),
            ],
        ],
    )
    return kb
