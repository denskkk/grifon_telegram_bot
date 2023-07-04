from aiogram.dispatcher.filters.state import StatesGroup, State


class Estate(StatesGroup):
    user_id = State()
    name = State()
    lang = State()
    estates = State()
    rooms = State()
    money = State()
    area = State()
    phone_num = State()
    finish = State()
    cancel = State()


class Admin(StatesGroup):
    delete_id = State()
    order_name = State()
    order_phone_num = State()
    order_comment = State()
