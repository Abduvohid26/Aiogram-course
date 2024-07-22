from aiogram import types, Dispatcher, Bot
import asyncio
from analise import has_cyrillic
from baza import to_cyrillic, to_latin
from aiogram import F
import time
from read import word_reader
import os
token = '6854957942:AAFI0xnaeg1fB0ur-Cp8XGgy3r7szCBCLpA'

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(F.text)
async def get_message(msg: types.Message):
    text = msg.text
    if has_cyrillic(text=text):
        await msg.answer(to_latin(text=text))
    else:
        await msg.answer(to_cyrillic(text=text))


@dp.message(F.document)
async def get_document(message: types.Message):
    document = message.document
    file_name = str(document.file_name)
    file_size = document.file_size
    file_id = document.file_id
    file_type = str(document.mime_type)
    document_type = file_name[file_name.rindex('.') + 1:]
    if document_type == 'docx':
        import time
        custom_name = f"{message.from_user.id}_{time.time()}.docx"
        file = await bot.get_file(file_id=file_id)
        await bot.download(file=file, destination=custom_name)
        green = '🟩'
        white = '⬜️'
        data = await message.answer("Fayl qabul qilindi")
        for i in range(1, 11):
            await data.edit_text(f"Fayl serverga yuklanmoqda...\n" 
                                 f"{i * green}{(10 - i) * white}")
        await data.delete()
        word_reader(file=custom_name)
        new_document = types.input_file.FSInputFile(path=custom_name, filename=file_name)
        await bot.send_chat_action(chat_id=message.chat.id, action='upload_document')
        await message.answer_document(document=new_document, caption="Rahmat botdan foydalanganiz uchun!")
        try:
            if os.path.isfile(custom_name):
                os.remove(custom_name)
        except:
            pass

    else:
        await message.answer("Iltimos Word(.docx) tipidagi fayl tashang!")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
