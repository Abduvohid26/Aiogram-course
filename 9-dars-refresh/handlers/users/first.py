from aiogram import types, Router, F
router_first = Router()


@router_first.message(F.text)
async def first_message(msg: types.Message):
    await msg.answer('NIma gap')
