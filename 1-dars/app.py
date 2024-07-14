from aiogram import types, Dispatcher, Bot
import asyncio
from aiogram import html
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    file = types.input_file.URLInputFile(url='https://www.autocar.co.uk/sites/autocar.co.uk/files/styles/gallery_slide/'
                        'public/images/car-reviews/first-drives/legacy/rolls_royce_phantom_top_10.jpg?itok=XjL9f1tx', filename='abduvohid')
    await message.answer_photo(file)
    # file = types.input_file.FSInputFile(path='test.jpg', filename='Abduvohid')
    # await message.answer_photo(file)
    # image = open('test.jpg', 'rb')
    # file = types.input_file.BufferedInputFile(file=image.read(), filename='Bu  mening rasmim')
    # await message.answer_photo(photo=file)
    # text = html.bold('Assalamu Aleykum')
    # await message.answer(text)
    # await message.answer(f'<a href="https://t.me/abduvohid_coder">Assalamu Aleykum</a>', parse_mode='HTML')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
