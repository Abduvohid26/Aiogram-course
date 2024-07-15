from aiogram import types, Dispatcher, Bot
import asyncio
from aiogram.filters import Command, CommandStart, CommandObject
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: types.Message, command: CommandObject):
    # data = command.args
    # print(data)
    await bot.send_message(text=f'Assalamu Aleykum {message.from_user.username}', chat_id=message.from_user.id)


@dp.message(Command('help'))
async def start(message: types.Message):
    await bot.send_message(text='Sizga qanday yordam beray', chat_id=message.from_user.id)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
