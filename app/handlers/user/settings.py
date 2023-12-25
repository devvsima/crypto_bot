from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandSettings, Text
from app.keyboards.inline_keyboard import settings_ikb
from database.users import set_user_notification

@dp.message_handler(Text("⚙️ Settings"))
@dp.message_handler(CommandSettings())
async def comm_settings(message: types.Message):
    await message.answer(
        text=_("⚙️ You settings:"),
        reply_markup= await settings_ikb(),
    )

@dp.callback_query_handler(Text("settings_notification_on"))
@dp.callback_query_handler(Text("settings_notification_off"))
async def settings_notification(callback: types.CallbackQuery):
    print(callback.data)
    if callback.data == "settings_notification_on":
        await set_user_notification(callback.from_user.id, True)
        print('set_true')
    elif callback.data == "settings_notification_off":
        await set_user_notification(callback.from_user.id, False)
        print('set_false')

    await callback.answer(text='Ok')


