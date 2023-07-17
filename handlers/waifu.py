from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
import waifu

from callbacks.waifu import WaifuTypeCallbackData, WaifuCategoryCallbackData
from keyboards.inline import sfw_categories_inline_keyboard, nsfw_categories_inline_keyboard
from states.waifu import WaifuTypeStatesGroup

waifu_router = Router()


@waifu_router.callback_query(WaifuTypeCallbackData.filter())
async def handle_waifu_type(query: CallbackQuery, callback_data: WaifuTypeCallbackData, state: FSMContext):
    if callback_data.type == 'sfw':
        await state.set_state(WaifuTypeStatesGroup.sfw)
        await query.message.answer('Вы выбрали обычные картинки. Выберите категорию',
                                   reply_markup=sfw_categories_inline_keyboard)
    else:
        await state.set_state(WaifuTypeStatesGroup.nsfw)
        await query.message.answer('Вы погрязли в разврате. Выбирайте категорию',
                                   reply_markup=nsfw_categories_inline_keyboard)


@waifu_router.callback_query(WaifuCategoryCallbackData.filter(), StateFilter(WaifuTypeStatesGroup.sfw))
async def handle_sfw_category(query: CallbackQuery, callback_data: WaifuCategoryCallbackData, state: FSMContext):
    category = callback_data.category
    async with waifu.WaifuAioClient() as session:
        image = await session.sfw(category)
    await query.message.answer_photo(image, reply_markup=sfw_categories_inline_keyboard)

