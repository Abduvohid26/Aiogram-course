import os

from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram import F
from gtts import gTTS
import asyncio
from custom_filter import CheckInstaLink, CheckReklama
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(msg: types.Message):
    await msg.answer(f'Assalamu Aleykum {msg.chat.username}')


@dp.message(F.text)
async def get_message(msg: types.Message):
    print(msg.text)
    tts = gTTS(msg.text, lang='en')
    tts.save(f'{msg.chat.id}.mp3')
    file = types.input_file.FSInputFile(path=f'{msg.chat.id}.mp3')
    await msg.answer_voice(voice=file)
    try:
        os.remove(f'{msg.chat.id}.mp3')
    except:
        pass


# @dp.message(CheckReklama(['@', 'http', 'https']))
# async def test(msg: types.Message):
#     await msg.answer('Reklama tashama')
#
#
# @dp.message(CheckInstaLink())
# async def test(msg: types.Message):
#     await msg.answer('INsta link')


# @dp.message(F.from_user.id.in_({816660001, }))
# @dp.message(F.text.in_({'abduvohid'}))


# @dp.message(F.text.contains('@'))
# async def echo(msg: types.Message):
#     # print(msg.from_user.json())
#     # print(msg.text)
#     await msg.answer('NIma gap')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

