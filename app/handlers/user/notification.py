from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import Text
from database.users import get_users_notification,get_favorite_list
from app.others.binance import get_user_well
from app.keyboards.inline_keyboard import edit_list_ikb
import schedule
import asyncio

async def run_pending():
    schedule.every(1).day.at("16:37", "Europe/Kyiv").do(lambda: asyncio.create_task(send_notification()))
    while True:
        schedule.run_pending()
        await asyncio.sleep(0)
        
async def send_notification():
    try:
        for usr_id in await get_users_notification():   
            fav_list = await get_favorite_list(usr_id['_id'])
            await bot.send_message(text=get_user_well(fav_list),
                                reply_markup=await edit_list_ikb(),
                                chat_id=usr_id['_id'])
    except:
        pass
