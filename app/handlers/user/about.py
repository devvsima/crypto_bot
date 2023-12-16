from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text, Command
from database.users import add_favorite_list, get_favorite_list
from app.others.binance import get_user_well

@dp.message_handler(Text("📔 About coins"))
@dp.message_handler(Command('about'))
async def about_coin(message: types.Message):

    await message.answer(text="about")

