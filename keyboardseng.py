from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# -------Клиентская часть на английском-------

# Главное меню
btnAbout = InlineKeyboardButton(
    "❔ Learn about us", callback_data='menu_about')
btnEstate = InlineKeyboardButton(
    "🏡 Find estate", callback_data='menu_estate')
btnManagers = InlineKeyboardButton(
    "📱 Order a call", callback_data='menu_managers')
btnCatalog = InlineKeyboardButton(
    "🏘 Catalog of estate", url='https://www.olx.ua/nedvizhimost/od/')
menu_markup = InlineKeyboardMarkup(row_width=1).add(
    btnAbout, btnEstate, btnManagers, btnCatalog)

# Раздел О нас
btnSite = InlineKeyboardButton(
    "🌐 Our site", url="https://www.grifonagency.com/")
btnAboutBack = InlineKeyboardButton("◀ Back", callback_data='about_back')
about_markup = InlineKeyboardMarkup(row_width=2).add(btnSite, btnAboutBack)

# Раздел Подобрать жилье

btnBuy = InlineKeyboardButton(
    "Buy estate", callback_data='estate_buy')
btnSell = InlineKeyboardButton(
    "Sell estate", callback_data='estate_sell')
btnRent = InlineKeyboardButton("Rent estate", callback_data='estate_rent')
btnRentOut = InlineKeyboardButton(
    "Rent out estate", callback_data='estate_rent_out')
btnEstateBack = InlineKeyboardButton("◀ Back", callback_data='estate_back')
estate_markup = InlineKeyboardMarkup(row_width=1).add(
    btnBuy, btnSell, btnRent, btnRentOut, btnEstateBack)

# Выбор количества комнат

btnRoomOne = InlineKeyboardButton("1", callback_data='room_1')
btnRoomTwo = InlineKeyboardButton("2", callback_data='room_2')
btnRoomThree = InlineKeyboardButton("3", callback_data='room_3')
btnRoomFour = InlineKeyboardButton("4+", callback_data='room_4more')
btnRoomBack = InlineKeyboardButton("◀ Back", callback_data='room_back')

rooms_markup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btnRoomOne, btnRoomTwo, btnRoomThree, btnRoomFour, btnRoomBack)

# Клавиатура аренды
btnRentOne = InlineKeyboardButton("Up to $ 350", callback_data="pricerent_one")
btnRentTwo = InlineKeyboardButton("350 - 500 $", callback_data="pricerent_two")
btnRentThree = InlineKeyboardButton(
    "500 - 700 $", callback_data="pricerent_three")
btnRentFour = InlineKeyboardButton(
    "700 - 1000 $", callback_data="pricerent_four")
btnRentFive = InlineKeyboardButton(
    "Higher than $ 1,000", callback_data="pricerent_five")
btnRentBack = InlineKeyboardButton("◀ Back", callback_data="pricerent_back")
rent_markup = InlineKeyboardMarkup(
    resize_keyboard=True, row_width=1).add(btnRentOne, btnRentTwo, btnRentThree, btnRentFour, btnRentFive, btnRentBack)

# Клавиатура продажи
btnBuyOne = InlineKeyboardButton(
    "Up to 25.000 $", callback_data='pricebuy_one')
btnBuyTwo = InlineKeyboardButton(
    "25.000 - 45.000 $ ", callback_data='pricebuy_two')
btnBuyThree = InlineKeyboardButton(
    "45.000 - 65.000 $", callback_data='pricebuy_three')
btnBuyFour = InlineKeyboardButton(
    "65.000 - 90.000 $", callback_data='pricebuy_four')
btnBuyFive = InlineKeyboardButton(
    "90.000 - 130.000 $", callback_data='pricebuy_five')
btnBuySix = InlineKeyboardButton(
    "Higher than 130.000 $", callback_data='pricebuy_six')
btnBuyBack = InlineKeyboardButton("◀ Back", callback_data="pricebuy_back")
buy_markup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btnBuyOne, btnBuyTwo, btnBuyThree, btnBuyFour, btnBuyFive, btnBuySix, btnBuyBack)

# Выбор районов

btnSuvArea = InlineKeyboardButton("Suvorov area", callback_data='area_one')
btnPrimArea = InlineKeyboardButton("Primorskiy area", callback_data='area_two')
btnKievArea = InlineKeyboardButton("Kyiv area", callback_data='area_three')
btnMalinArea = InlineKeyboardButton(
    "Malinowski area", callback_data='area_four')
btnOdesRegion = InlineKeyboardButton(
    "Odessa region", callback_data='area_five')
btnAreaBack = InlineKeyboardButton("◀ Back", callback_data="area_back")

area_markup = InlineKeyboardMarkup(row_width=1).add(
    btnSuvArea, btnPrimArea, btnKievArea, btnMalinArea, btnOdesRegion, btnAreaBack)


# Клавиатура заказа звонка
order_call = KeyboardButton("Order a call")
cancel_order = KeyboardButton("◀ Back")
call_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(order_call, cancel_order)


# Запрос контакта
call_back_btn = KeyboardButton("❌ Cancel")
send_contact = KeyboardButton("☎️ Send your contact", request_contact=True)

contact_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(send_contact, call_back_btn)


yesbtn = InlineKeyboardButton("✅ Yes", callback_data='finish_yes')
nobtn = InlineKeyboardButton("✏ Edit", callback_data='finish_no')

finish_markup = InlineKeyboardMarkup().add(yesbtn, nobtn)

clear_markup = types.ReplyKeyboardRemove()

# комментарий
btnSkip = InlineKeyboardButton("⏭ Skip", callback_data='following_btn')
comment_markup = InlineKeyboardMarkup(row_width=1).add(btnSkip)
