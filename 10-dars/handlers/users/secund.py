from aiogram import types, Router, F
router_second = Router()


@router_second.message(F.text)
async def second_message(msg: types.Message):
    await msg.answer('NIma gap s')
