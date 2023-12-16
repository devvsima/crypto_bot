from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text, Command
from app.keyboards.inline_keyboard import about_ikb
from database.about import get_about_coin

@dp.message_handler(Text("📔 About coins"))
@dp.message_handler(Command('about'))
async def about_coins(message: types.Message):
    await message.answer(text="about", reply_markup=await about_ikb())

@dp.callback_query_handler(Text(endswith="_about"))
async def about_coin_info(callback: types.CallbackQuery):
    coin = callback.data.replace("_about", "")
    about_coin = await get_about_coin(coin)
    await callback.message.answer(text=f"<blockquote>{coin}</blockquote>\n{about_coin}")
