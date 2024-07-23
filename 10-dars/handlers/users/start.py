from aiogram.filters import CommandStart
from loader import dp, bot
from aiogram import types

@dp.message(CommandStart())
async def start_bot(message: types.Message):
    await message.answer(f'Assalamu Aleykum {message.from_user.full_name}')