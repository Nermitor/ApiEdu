from aiogram import BaseMiddleware

from API.waifu import WaifuApi


class WaifuApiMiddleWare(BaseMiddleware):
    """Передаёт хендлерам объект WaifuApi"""

    def __init__(self, waifu_api: WaifuApi):
        self.waifu_api = waifu_api

    async def __call__(self, handler, event, data):
        data['waifu_api'] = self.waifu_api
        return await handler(event, data)