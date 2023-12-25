from aiogram import types, Dispatcher
from loader import dp, bot, _
from aiogram.dispatcher.filters import CommandHelp


@dp.message_handler(commands="🆘 Help")
@dp.message_handler(CommandHelp())
async def comm_start(message: types.Message):
    await message.answer(
        text=_("To view the rate of the coin you are interested in you can write its name for example (BTC),\
                you will see the current rate in USDT and will be able to add it to your list of 'Favorites' cryptocurrencies.\
                \nEvery day at a certain time you will receive notifications, if you do not want to receive them, then disable them in the settings.")
                )
