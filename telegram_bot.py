from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5813801806:AAHDGmewaQ7IysZrw4xo61pnQneWon1R9nQ'
coz = ('Because', 'because', 'coz')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Hi \n i am a new bot')


@dp.message_handler()
async def litile_boy_simulyator(message: types.Message):
    if message.text not in coz:
        ask = 'Why'    
        await message.answer(ask)
    else:
        await message.answer('Ok')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)