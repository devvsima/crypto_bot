from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text, Command
from database.users import add_favorite_list, get_favorite_list
from app.others.binance import get_user_well
from app.keyboards.inline_keyboard import edit_list_ikb


@dp.callback_query_handler(Text(endswith="_add"))
async def favorite(callback: types.CallbackQuery):
    edit_data = callback.data.replace("_add", "")
    await add_favorite_list(callback.from_user.id, edit_data)
    await callback.answer('Added')


@dp.message_handler(Text("⭐️ Favorites"))
@dp.message_handler(Command('favorites'))
async def favorite_list(message: types.Message):
    fav_list = await get_favorite_list(message.from_user.id)
    print(fav_list)
    await message.answer(text=get_user_well(fav_list),
                         reply_markup=await edit_list_ikb())

