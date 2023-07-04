from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# -------Клиентская часть на украинском-------

# Главное меню
btnAbout = InlineKeyboardButton(
    "❔ Дізнатись про нас", callback_data='menu_about')
btnEstate = InlineKeyboardButton(
    "🏡 Підібрати житло", callback_data='menu_estate')
btnManagers = InlineKeyboardButton(
    "📱 Замовити дзвінок", callback_data='menu_managers')
btnCatalog = InlineKeyboardButton(
    "🏘 Каталог об'єктів", url='https://www.olx.ua/nedvizhimost/od/')
menu_markup = InlineKeyboardMarkup(row_width=1).add(
    btnAbout, btnEstate, btnManagers, btnCatalog)

# Раздел О нас
btnSite = InlineKeyboardButton(
    "🌐 Наш сайт", url="https://www.grifonagency.com/")
btnAboutBack = InlineKeyboardButton("◀ Назад", callback_data='about_back')
about_markup = InlineKeyboardMarkup(row_width=2).add(btnSite, btnAboutBack)

# Раздел Подобрать жилье

btnBuy = InlineKeyboardButton(
    "Купити нерухомість", callback_data='estate_buy')
btnSell = InlineKeyboardButton(
    "Продати нерухомість", callback_data='estate_sell')
btnRent = InlineKeyboardButton("Зняти житло", callback_data='estate_rent')
btnRentOut = InlineKeyboardButton(
    "Здати в оренду житло", callback_data='estate_rent_out')
btnEstateBack = InlineKeyboardButton("◀ Назад", callback_data='estate_back')
estate_markup = InlineKeyboardMarkup(row_width=1).add(
    btnBuy, btnSell, btnRent, btnRentOut, btnEstateBack)

# Выбор количества комнат

btnRoomOne = InlineKeyboardButton("1", callback_data='room_1')
btnRoomTwo = InlineKeyboardButton("2", callback_data='room_2')
btnRoomThree = InlineKeyboardButton("3", callback_data='room_3')
btnRoomFour = InlineKeyboardButton("4+", callback_data='room_4more')
btnRoomBack = InlineKeyboardButton("◀ Назад", callback_data='room_back')

rooms_markup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btnRoomOne, btnRoomTwo, btnRoomThree, btnRoomFour, btnRoomBack)

# Клавиатура аренды
btnRentOne = InlineKeyboardButton("До 350 $", callback_data="pricerent_one")
btnRentTwo = InlineKeyboardButton("350 - 500 $", callback_data="pricerent_two")
btnRentThree = InlineKeyboardButton(
    "500 - 700 $", callback_data="pricerent_three")
btnRentFour = InlineKeyboardButton(
    "700 - 1000 $", callback_data="pricerent_four")
btnRentFive = InlineKeyboardButton(
    "Вище за 1000 $", callback_data="pricerent_five")
btnRentBack = InlineKeyboardButton("◀ Назад", callback_data="pricerent_back")
rent_markup = InlineKeyboardMarkup(
    resize_keyboard=True, row_width=1).add(btnRentOne, btnRentTwo, btnRentThree, btnRentFour, btnRentFive, btnRentBack)

# Клавиатура продажи
btnBuyOne = InlineKeyboardButton(
    "До 25.000 $", callback_data='pricebuy_one')
btnBuyTwo = InlineKeyboardButton(
    "25.000 - 45.000 $ ", callback_data='pricebuy_two')
btnBuyThree = InlineKeyboardButton(
    "45.000 - 65.000 $", callback_data='pricebuy_three')
btnBuyFour = InlineKeyboardButton(
    "65.000 - 90.000 $", callback_data='pricebuy_four')
btnBuyFive = InlineKeyboardButton(
    "90.000 - 130.000 $", callback_data='pricebuy_five')
btnBuySix = InlineKeyboardButton(
    "Від 130.000 $", callback_data='pricebuy_six')
btnBuyBack = InlineKeyboardButton("◀ Назад", callback_data="pricebuy_back")
buy_markup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btnBuyOne, btnBuyTwo, btnBuyThree, btnBuyFour, btnBuyFive, btnBuySix, btnBuyBack)


# Выбор районов

btnSuvArea = InlineKeyboardButton("Суворовський", callback_data='area_one')
btnPrimArea = InlineKeyboardButton("Приморський", callback_data='area_two')
btnKievArea = InlineKeyboardButton("Київський", callback_data='area_three')
btnMalinArea = InlineKeyboardButton("Малиновський", callback_data='area_four')
btnOdesRegion = InlineKeyboardButton(
    "Одеська область", callback_data='area_five')
btnAreaBack = InlineKeyboardButton("◀ Назад", callback_data="area_back")

area_markup = InlineKeyboardMarkup(row_width=1).add(
    btnSuvArea, btnPrimArea, btnKievArea, btnMalinArea, btnOdesRegion, btnAreaBack)


# Клавиатура заказа звонка
order_call = KeyboardButton("Замовити дзвінок")
cancel_order = KeyboardButton("◀ Назад")
call_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(order_call, cancel_order)


# Запрос контакта
call_back_btn = KeyboardButton("❌ Cкасування")
send_contact = KeyboardButton("☎️ Надіслати контакт", request_contact=True)
contact_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(send_contact, call_back_btn)


yesbtn = InlineKeyboardButton("✅ Так", callback_data='finish_yes')
nobtn = InlineKeyboardButton("✏ Редагувати", callback_data='finish_no')

finish_markup = InlineKeyboardMarkup().add(yesbtn, nobtn)

clear_markup = types.ReplyKeyboardRemove()

# комментарий
btnSkip = InlineKeyboardButton("⏭ Пропустити", callback_data='following_btn')
comment_markup = InlineKeyboardMarkup(row_width=1).add(btnSkip)
