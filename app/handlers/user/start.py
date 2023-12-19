from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from loader import dp, bot, _
from database.users import add_user
from app.keyboards.keyboard import base_kb
@dp.message_handler(CommandStart())
async def comm_start(message: types.Message):
    text = _(f"👋, <a href='tg://user?id={message.from_user.id}'>{(message.from_user.full_name)}</a>")
    await add_user(id=message.from_user.id)
    await message.answer(text, 
                         reply_markup=await base_kb()
                         )
    

    from database.users import get_users_notification
    print(await get_users_notification())

