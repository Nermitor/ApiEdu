from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from waifu import ImageCategories

from callbacks.waifu import WaifuCategoryCallbackData, WaifuTypeCallbackData

sfw_categories_inline_keyboard_builder = InlineKeyboardBuilder()
for sfw_category in ImageCategories['sfw']:
    sfw_categories_inline_keyboard_builder.button(
        text=sfw_category,
        callback_data=WaifuCategoryCallbackData(category=sfw_category)
    )  # Потом поменяем колбэк
sfw_categories_inline_keyboard = sfw_categories_inline_keyboard_builder.adjust(4).as_markup()

waifu_type_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='sfw',
        callback_data=WaifuTypeCallbackData(type='sfw')
    ), InlineKeyboardButton(
        text='nsfw',
        callback_data=WaifuTypeCallbackData(type='nsfw')
    )]
])
