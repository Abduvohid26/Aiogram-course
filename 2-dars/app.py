from aiogram import types, Dispatcher, Bot
import asyncio
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message()
async def start(message: types.Message):
    # await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    # document = open('test.docx', 'rb')
    # file = types.input_file.BufferedInputFile(file=document.read(), filename='Abduvohid.docx')
    # await message.answer_document(document=file)
    # await message.answer_dice(emoji='🎯')
    data = await bot.send_message(chat_id=message.from_user.id, text='Yuklanmoqda...')
    for i in range(1, 11):
        percent = i * 10
        black = '⬛️'
        white = '⬜️'
        await data.edit_text(text=f'{i*black}{white*(10-i)}\n'
                             f'{percent} % yuklandi')
    await data.delete()
    await message.answer('Tayyor')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
