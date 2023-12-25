from aiogram.types import (
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from database import about, users


async def base_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Название", callback_data="callback"),
            ],
        ],
    )
    return ikb

async def sub_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Канал 1", url="https://t.me/+7lZSbqjjRHEwOGMy"),
            ],
            [
                InlineKeyboardButton(text="Проверить", callback_data="sub_check"),
            ],
        ],
    )
    return ikb

async def add_favorite_ikb(coin):
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⭐️Add to favorite", callback_data=f"{coin}_add"),
            ],
        ],
        )
    return ikb


async def about_ikb():
    ikb = InlineKeyboardMarkup()
    for i in await about.get_coins_list():
        ikb.add(InlineKeyboardButton(text=i, callback_data=f"{i}_about"))
    return ikb

async def edit_list_ikb():
    ikb = InlineKeyboardMarkup()
    ikb.add(InlineKeyboardButton(text='✏️ Edit', callback_data='edit_list'))
    return ikb

async def delete_favorite_ikb(id):
    ikb = InlineKeyboardMarkup()
    for i in await users.get_favorite_list(id):
        ikb.add(InlineKeyboardButton(text=i, callback_data=f"{i}_del"))
    return ikb

async def settings_ikb():
    ikb = InlineKeyboardMarkup(
        resize_keyboard=True,
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔔", callback_data=f"settings_notification_on"),
                InlineKeyboardButton(text="🔕", callback_data=f"settings_notification_off"),
            ],
        ],
        )
    return ikb