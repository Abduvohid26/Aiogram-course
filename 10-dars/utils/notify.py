from loader import bot, dp
from data.config import ADMINS


async def start_up():
    for i in ADMINS:
        await bot.send_message(i, 'Bot has started!')


async def shut_up():
    for i in ADMINS:
        await bot.send_message(i, 'Bot has finished!')
