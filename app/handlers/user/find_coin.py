from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandHelp
from app.others.binance import searc_coin
from app.keyboards.inline_keyboard import add_favorite

@dp.message_handler()
async def comm_start(message: types.Message):
    user_msg = message.text.upper()
    user_msg += "USDT"
    try:
        text = searc_coin(user_msg)
        await message.answer(
            text=text,
            reply_markup=await add_favorite(user_msg)
        )
    except:
        error_text = 'Coin nor found!\nTry again.'
        await message.answer(
            text=error_text,
        )
