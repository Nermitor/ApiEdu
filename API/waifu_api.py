from API.base import BaseApi


class WaifuApi(BaseApi):
    async def get_waifu(self, category: str, nsfw=False):

        if nsfw:
            waifu_type = 'nsfw'
        else:
            waifu_type = 'sfw'

        answer = await self.get(f'https://api.waifu.pics/{waifu_type}/{category}')
        return answer['url']


waifu_api = WaifuApi()
