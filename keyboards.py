from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# -------Админская часть-------

# Клавиатура главной админки
btnDelete = InlineKeyboardButton(
    "🗑 Удалить заявку", callback_data='admin_delete')
btnAdminExit = InlineKeyboardButton(
    "Выйти с панели админа", callback_data='admin_exit')
btnBids = InlineKeyboardButton(
    "📖 Заявки", url='https://docs.google.com/spreadsheets/d/1vkBpMw2fpXL5yUM1jQL8IBihddWtDmwCTF1covW7dm8/edit')
admin_main_markup = InlineKeyboardMarkup(
    row_width=2).add(btnBids, btnDelete, btnAdminExit)

# Клавиатура удаления в админке
btnAdminCancel = InlineKeyboardButton("❌ Отмена", callback_data='sub_cancel')
admin_sub_markup = InlineKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(btnAdminCancel)

# Клавиатура принятия заявки
btnConnect = InlineKeyboardButton(
    "✅ Принять заявку", callback_data="bid_connect")
admin_chat_markup = InlineKeyboardMarkup().add(btnConnect)

btnBidReject = InlineKeyboardButton(
    "❌ Отказаться от заявки", callback_data="bidmenu_reject")
admin_bid_markup = InlineKeyboardMarkup(
    row_width=1).add(btnBidReject)

btnDetails = InlineKeyboardButton(
    "ℹ Детали заявки", url='https://docs.google.com/spreadsheets/d/1vkBpMw2fpXL5yUM1jQL8IBihddWtDmwCTF1covW7dm8/edit')
details_markup = InlineKeyboardMarkup().add(btnDetails)
# -------Клиентская часть-------

# Запрос языка
btnRus = InlineKeyboardButton("🇷🇺 Русский язык", callback_data='lang_ru')
btnUA = InlineKeyboardButton("​🇺🇦 Украинский язык", callback_data='lang_ua')
btnEng = InlineKeyboardButton("🇬🇧 English language", callback_data='lang_eng')
lang_markup = InlineKeyboardMarkup(row_width=2).add(btnUA, btnRus, btnEng)

# Главное меню
btnAbout = InlineKeyboardButton("❔ Узнать о нас", callback_data='menu_about')
btnEstate = InlineKeyboardButton(
    "🏡 Подобрать жилье", callback_data='menu_estate')
btnManagers = InlineKeyboardButton(
    "📱 Заказать звонок", callback_data='menu_managers')
btnCatalog = InlineKeyboardButton(
    "🏘 Каталог объектов", url='https://www.olx.ua/nedvizhimost/od/')
menu_markup = InlineKeyboardMarkup(row_width=1).add(
    btnAbout, btnEstate, btnManagers, btnCatalog)

# Раздел О нас
btnSite = InlineKeyboardButton(
    "🌐 Наш сайт", url="https://www.grifonagency.com/")
btnAboutBack = InlineKeyboardButton("◀ Назад", callback_data='about_back')
about_markup = InlineKeyboardMarkup(row_width=2).add(btnSite, btnAboutBack)

# Раздел Подобрать жилье

btnBuy = InlineKeyboardButton(
    "Приобрести недвижимость", callback_data='estate_buy')
btnSell = InlineKeyboardButton(
    "Продать недвижимость", callback_data='estate_sell')
btnRent = InlineKeyboardButton("Снять жилье", callback_data='estate_rent')
btnRentOut = InlineKeyboardButton(
    "Сдать в аренду жилье", callback_data='estate_rent_out')
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
    "Выше 1000 $", callback_data="pricerent_five")
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
    "От 130.000 $", callback_data='pricebuy_six')
btnBuyBack = InlineKeyboardButton("◀ Назад", callback_data="pricebuy_back")
buy_markup = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    btnBuyOne, btnBuyTwo, btnBuyThree, btnBuyFour, btnBuyFive, btnBuySix, btnBuyBack)

# Выбор районов

btnSuvArea = InlineKeyboardButton("Суворовский", callback_data='area_one')
btnPrimArea = InlineKeyboardButton("Приморский", callback_data='area_two')
btnKievArea = InlineKeyboardButton("Киевский", callback_data='area_three')
btnMalinArea = InlineKeyboardButton("Малиновский", callback_data='area_four')
btnOdesRegion = InlineKeyboardButton(
    "Одесская область", callback_data='area_five')
btnAreaBack = InlineKeyboardButton("◀ Назад", callback_data="area_back")

area_markup = InlineKeyboardMarkup(row_width=1).add(
    btnSuvArea, btnPrimArea, btnKievArea, btnMalinArea, btnOdesRegion, btnAreaBack)


# Клавиатура заказа звонка
order_call = KeyboardButton("Заказать звонок")
cancel_order = KeyboardButton("◀ Назад")
call_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(order_call, cancel_order)


# Запрос контакта
call_back_btn = KeyboardButton("❌ Отмена")
send_contact = KeyboardButton("☎️ Отправить контакт", request_contact=True)
contact_markup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(send_contact, call_back_btn)


# Запрос верности введенного
yesbtn = InlineKeyboardButton("✅ Да", callback_data='finish_yes')
nobtn = InlineKeyboardButton("✏ Редактировать", callback_data='finish_no')

finish_markup = InlineKeyboardMarkup().add(yesbtn, nobtn)

# Удаление клавиатуры
clear_markup = types.ReplyKeyboardRemove()

# комментарий
btnSkip = InlineKeyboardButton("⏭ Пропустить", callback_data='following_btn')
comment_markup = InlineKeyboardMarkup(row_width=1).add(btnSkip)
