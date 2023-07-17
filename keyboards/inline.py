from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from waifu import ImageCategories

from callbacks.waifu import WaifuCategoryCallbackData, WaifuTypeCallbackData


# Клавиатура для sfw
sfw_categories_inline_keyboard_builder = InlineKeyboardBuilder()
for sfw_category in ImageCategories['sfw']:
    sfw_categories_inline_keyboard_builder.button(
        text=sfw_category,
        callback_data=WaifuCategoryCallbackData(category=sfw_category).pack()
    )
sfw_categories_inline_keyboard = sfw_categories_inline_keyboard_builder.adjust(4).as_markup()


# Клавиатура для nsfw
nsfw_categories_inline_keyboard_builder = InlineKeyboardBuilder()
for nsfw_category in ImageCategories['nsfw']:
    nsfw_categories_inline_keyboard_builder.button(
        text=nsfw_category,
        callback_data=WaifuCategoryCallbackData(category=nsfw_category).pack()
    )
nsfw_categories_inline_keyboard = nsfw_categories_inline_keyboard_builder.adjust(4).as_markup()


waifu_type_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='Обычные',
        callback_data=WaifuTypeCallbackData(type='sfw').pack()
    ), InlineKeyboardButton(
        text='18+',
        callback_data=WaifuTypeCallbackData(type='nsfw').pack()
    )]
])
