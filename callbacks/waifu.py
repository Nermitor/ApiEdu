from aiogram.filters.callback_data import CallbackData


class WaifuTypeCallbackData(CallbackData, prefix='waifu_type'):
    type: str  # 'nsfw' | 'sfw'


class WaifuCategoryCallbackData(CallbackData, prefix='waifu_category'):
    category: str
