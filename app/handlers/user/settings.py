from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandSettings, Text

@dp.message_handler(Text("⚙️ Settings"))
@dp.message_handler(CommandSettings())
async def comm_start(message: types.Message):
    await message.answer(
        text=_("⚙️ You settings:"),
    )
