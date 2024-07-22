from aiogram import types, Bot, Dispatcher
import asyncio
from aiogram import F
from aiogram.filters import CommandStart
import time
from moviepy.editor import *
token = '6854957942:AAE4e1dVzv4n0x4XIyayqMmiIM_e_PCmizI'
bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_bot(msg: types.Message):
    await msg.answer('Assalamu Aleykum')


@dp.message(F.video)
async def test(message:types.Message):
    height = message.video.height
    width = message.video.width
    file_id = message.video.file_id
    filename = message.video.file_name
    file_size = (message.video.file_size) / (1024*1024)
    file_type = message.video.mime_type
    duration = message.video.duration
    if duration > 60:
        await message.answer("Iltimos 1 daqiqali video yuboring!")
    else:
        if file_size > 10:
            await message.answer("Iltimos video hajmi 10 MB gacha bo'lsin!")
        else:
            file = await bot.get_file(file_id=file_id)
            custom_file_name = f"{message.from_user.id}_{time.time()}.mp4"
            await bot.download(file=file, destination=custom_file_name)
            clip = VideoFileClip(filename=custom_file_name)
            target_width = 640
            target_height = 640
            resize_video = clip.resize((target_height, target_width))
            custom_file_name2 = f"{message.from_user.id}_{time.time()}.mp4"
            resize_video.write_videofile(custom_file_name2, codec='libx264')
            sending_file = types.input_file.FSInputFile(path=custom_file_name2, filename=filename)
            await bot.send_chat_action(action='upload_video_note', chat_id=message.chat.id)
            await message.answer_video_note(video_note=sending_file)
            try:
                if os.path.isfile(custom_file_name2):
                    os.remove(custom_file_name2)
                if os.path.isfile(custom_file_name):
                    os.remove(custom_file_name)
            except:
                pass


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

