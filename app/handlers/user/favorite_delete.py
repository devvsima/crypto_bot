from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text, Command
from database.users import del_favorite_list_coin
from app.keyboards.inline_keyboard import delete_favorite_ikb

@dp.callback_query_handler(Text("edit_list"))
async def edit_list(callback: types.CallbackQuery):
    await callback.message.answer(text=f"Select the coin to delete:",
                                  reply_markup=await delete_favorite_ikb(callback.from_user.id))

@dp.callback_query_handler(Text(endswith="_del"))
async def delete_list_coin(callback: types.CallbackQuery):
    coin = callback.data.replace("_del", "")
    await del_favorite_list_coin(id=callback.from_user.id,
                                 coin=coin)
    await callback.answer(text=f"Coin delete")
