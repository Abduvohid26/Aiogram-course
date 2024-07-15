from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram import F
from datetime import datetime
from rembg import remove
from PIL import Image
import asyncio
import time
import requests
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(msg: types.Message):
    await msg.answer(f'Assalamu Aleykum')


@dp.message(F.text)
async def echo(msg: types.Message):
    await msg.answer('Nima gap !!!')


@dp.message(F.photo)
async def get_photo(msg: types.Message):
    photo = msg.photo[-1]
    file_id = photo.file_id
    width = photo.width
    height = photo.height
    file_size = photo.file_size
    # await msg.answer(f'Siz yuborgan rasm ma\'lumotlari\n'
    #                  f'file_id: {file_id}\n'
    #                  f'width: {width}\n'
    #                  f'height: {height}\n'
    #                  f'size: {file_size//1024}')
    # await msg.answer_photo(photo=file_id)
    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    url = f'https://api.telegram.org/file/bot/{token}/{file_path}'
    # await bot.download(file=file, destination=f'{datetime.now()}.jpg')
    vaqt = time.time()
    name = f'{msg.from_user.id}_{vaqt}'
    input_path = requests.get(url=url, stream=True).raw
    input = Image.open(input_path)
    output = remove(input)
    output.save(name)
    rasm = types.input_file.FSInputFile(path=name, filename='salom')
    await msg.answer_photo(photo=rasm)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


