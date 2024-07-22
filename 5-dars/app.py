from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram import F
from datetime import datetime
from rembg import remove
from PIL import Image
import asyncio
import time
import requests
from io import BytesIO
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

    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    url = f'https://api.telegram.org/file/bot/{token}/{file_path}'

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        input_path = BytesIO(response.content)
        input_image = Image.open(input_path)
        output_image = remove(input_image)

        # Create a unique filename
        timestamp = int(time.time())
        user_id = msg.from_user.id
        filename = f'{user_id}_{timestamp}.png'

        # Save the output image to a BytesIO object
        output_path = BytesIO()
        output_image.save(output_path, format='PNG')
        output_path.seek(0)

        # Send the processed image back to the user
        rasm = types.InputFile(output_path, filename=filename)
        await msg.answer_photo(photo=rasm)

    except Exception as e:
        await msg.answer(f"Rasmni qayta ishlashda xato yuz berdi: {e}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())


