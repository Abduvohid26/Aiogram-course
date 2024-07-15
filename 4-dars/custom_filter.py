from aiogram import types
from aiogram.filters import BaseFilter


class CheckInstaLink(BaseFilter):
    # def __init__(self, my_text: str):
    #     self.my_text = my_text

    async def __call__(self, msg: types.Message):
        if msg.text.startswith('https://instagram.com'):
            return True
        elif msg.text.startswith('https://www.instagram.com'):
            return True

        elif msg.text.startswith('http://www.instagram.com'):
            return True

        elif msg.text.startswith('http://instagram.com'):
            return True
        else:
            return False


class CheckReklama(BaseFilter):
    def __init__(self, my_text: list):
        self.urls = my_text

    async def __call__(self, msg: types.Message):
        for i in self.urls:
            if i in msg.text:
                return True

