from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text, Command
from database.users import add_favorite_list, get_favorite_list

@dp.callback_query_handler(Text(endswith="_add"))
async def favorite(callback: types.CallbackQuery):
    await callback.answer('ok')
    edit_data = callback.data.replace("_add", "")
    await add_favorite_list(callback.from_user.id, edit_data)

@dp.message_handler(Text("⭐️"))
@dp.message_handler(Command('favorite'))
async def favorite_list(message: types.Message):
    fav_list = await get_favorite_list(message.from_user.id)
