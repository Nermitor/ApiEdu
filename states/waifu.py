from aiogram.fsm.state import StatesGroup, State


class WaifuTypeStatesGroup(StatesGroup):
    sfw = State()
    nsfw = State()