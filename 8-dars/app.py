from aiogram import types, Bot, Dispatcher
from aiogram import F
from aiogram.filters import CommandStart
import asyncio
from geopy.geocoders import  Nominatim
token = '6854957942:AAGhUCBS5gYvagBH2ehlo6MOFieMWI37lpY'
bot = Bot(token=token)

dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(f'Assalamu Aleykum {message.from_user.username}')


# @dp.message(F.audio)
# async def echo(message: types.Message):
#     print(message.audio.json())
#     await message.answer('Botga audio yubordiz')

# @dp.message(F.animation)
# async def echo(message: types.Message):
#     print(message.animation.json())
#     await message.answer('Botga animation yubordiz')


# @dp.message(F.sticker)
# async def echo(message: types.Message):
#     print(message.sticker.json())
#     await message.answer('Botga sticker yubordiz')

#
# @dp.message(F.voice)
# async def echo(message: types.Message):
#     print(message.voice.json())
#     await message.answer('Botga voice yubordiz')


# @dp.message(F.video_note)
# async def echo(message: types.Message):
#     print(message.video_note.json())
#     await message.answer('Botga video_note yubordiz')

#
# @dp.message(F.contact)
# async def echo(message: types.Message):
#     print(message.contact.json())
#     await message.answer('Botga contact yubordiz')


@dp.message(F.location)
async def echo(message: types.Message):
    await get_location(lat=message.location.latitude, long=message.location.longitude)
    await message.answer('Botga location yubordiz')


async def get_location(lat, long):
    geolocator = Nominatim(user_agent="Abduvohid")
    location = geolocator.reverse(f'{lat}, {long}')
    print(location.address)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
