import waifu
from aiogram import Router
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from callbacks.waifu_callbacks import WaifuTypeCallbackData, WaifuCategoryCallbackData
from keyboards.inline import sfw_categories_inline_keyboard, nsfw_categories_inline_keyboard

waifu_router = Router()


@waifu_router.callback_query(WaifuTypeCallbackData.filter())
async def handle_waifu_type(query: CallbackQuery, callback_data: WaifuTypeCallbackData):
    if callback_data.type == 'sfw':
        await query.message.answer('Вы выбрали обычные картинки. Выберите категорию',
                                   reply_markup=sfw_categories_inline_keyboard)
    else:
        await query.message.answer('Вы погрязли в разврате. Выбирайте категорию',
                                   reply_markup=nsfw_categories_inline_keyboard)


@waifu_router.callback_query(WaifuCategoryCallbackData.filter())
async def handle_sfw_category(query: CallbackQuery, callback_data: WaifuCategoryCallbackData):
    category = callback_data.category
    waifu_type = callback_data.type
    async with waifu.WaifuAioClient() as session:
        if waifu_type == 'sfw':
            image = await session.sfw(category)
            keyboard = sfw_categories_inline_keyboard
        else:
            image = await session.nsfw(category)
            keyboard = nsfw_categories_inline_keyboard
    if image.endswith('.gif'):
        await query.message.answer_animation(image, reply_markup=keyboard)
    else:
        await query.message.answer_photo(image, reply_markup=keyboard)


#  Написать обработчик команды /waifu {type} {category}
@waifu_router.message(Command('waifu'))
async def get_waifu_command(message: Message):
    words = message.text.split()[1:]
    if len(words) == 2:
        waifu_type = words[0]
        waifu_category = words[1]
        if waifu_type in ('sfw', 'nsfw') and waifu_category in waifu.ImageCategories[waifu_type]:
            async with waifu.WaifuAioClient() as session:
                if waifu_type == 'sfw':
                    image = await session.sfw(waifu_category)
                    keyboard = sfw_categories_inline_keyboard
                else:
                    image = await session.nsfw(waifu_category)
                    keyboard = nsfw_categories_inline_keyboard
            if image.endswith('.gif'):
                await message.answer_animation(image, reply_markup=keyboard)
            else:
                await message.answer_photo(image, reply_markup=keyboard)
        else:
            await message.answer('Возможно вы ввели недопустимый тип или категорию')
