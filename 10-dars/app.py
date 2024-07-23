from loader import dp, bot
import asyncio
from utils.notify import start_up, shut_up
import handlers
from utils.set_botcommands import commands
from handlers.users.first import first_message
from handlers.users.secund import second_message


async def main():
    try:
        dp.startup.register(start_up)
        dp.shutdown.register(shut_up)
        dp.include_router([first_message, second_message])
        await bot.set_my_commands(commands=commands)
        await dp.start_polling(bot)
    finally:
        await bot.session().close()


if __name__ == '__main__':
    asyncio.run(main())
