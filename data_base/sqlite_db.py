import sqlite3 as sq

from aiogram import types

import keyboards as kb

parse = []
del_check = False
update_check = False
call_name = ""
call_phone = ""
call_message = ""
call_comment = ""
call_lang = ""
base = sq.connect('users_req.db')
base2 = sq.connect('users_calls.db')
cur = base.cursor()
cur2 = base2.cursor()


def sql_start():
    global base, base2, cur, cur2
    if base:
        print('База1 подключена')
    if base2:
        print('База2 подключена')
    base.execute(
        'CREATE TABLE IF NOT EXISTS users(id INTEGER,name Text, contacts TEXT, estate TEXT, rooms TEXT, money TEXT, area TEXT, lang TEXT)')
    base.commit()
    base2.execute(
        'CREATE TABLE IF NOT EXISTS calls(id INTEGER, name TEXT, contacts TEXT, message TEXT, manager TEXT, lang TEXT, comment TEXT)')
    base2.commit()


# Добавление заявок на покупку


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)',
                    (data['user_id'], data['name'], data['phone_num'], data['estates'], data['rooms'], data['money'],
                     data['area'], data['lang']))
        base.commit()


# Добавление заказов на звонок


async def sql_add_call_command(state):
    async with state.proxy() as data:
        cur2.execute('INSERT INTO calls VALUES (?,?,?,?,?,?,?)',
                     (data['id'], data['name'], data['phone_num'], data['message_id'], data['manager'], data['lang'],
                      data['order_comment']))
        base2.commit()


async def sql_view1_call_command(bid_id):
    global call_name, call_phone, call_comment, call_lang
    revision = cur2.execute(
        "SELECT * FROM calls WHERE message == ?", [bid_id]).fetchone()
    if revision is not None:
        name = cur2.execute("SELECT name FROM calls WHERE message == ?", [
            bid_id]).fetchone()
        phone = cur2.execute("SELECT contacts FROM calls WHERE message == ?", [
            bid_id]).fetchone()
        comment = cur2.execute("SELECT comment FROM calls WHERE message == ?", [
            bid_id]).fetchone()
        lang = cur2.execute("SELECT lang FROM calls WHERE message == ?", [
            bid_id]).fetchone()
        call_name = name[0]
        call_phone = phone[0]
        call_comment = comment[0]
        call_lang = lang[0]


async def sql_view2_call_command(manager_id):
    global call_name, call_phone, call_message, call_comment, call_lang
    revision = cur2.execute(
        "SELECT * FROM calls WHERE manager == ?", [manager_id]).fetchone()
    if revision is not None:
        name = cur2.execute("SELECT name FROM calls WHERE manager == ?", [
            manager_id]).fetchone()
        phone = cur2.execute("SELECT contacts FROM calls WHERE manager == ?", [
            manager_id]).fetchone()
        message = cur2.execute("SELECT message FROM calls WHERE manager == ?", [
            manager_id]).fetchone()
        comment = cur2.execute("SELECT comment FROM calls WHERE manager == ?", [
            manager_id]).fetchone()
        lang = cur2.execute("SELECT lang FROM calls WHERE manager == ?", [
            manager_id]).fetchone()
        call_name = name[0]
        call_phone = phone[0]
        call_message = message[0]
        call_comment = comment[0]
        call_lang = lang[0]


async def sql_change_call_command(bid_id, manager_id):
    cur2.execute("UPDATE calls SET manager == ? WHERE message == ?",
                 (manager_id, bid_id))
    base2.commit()


async def sql_parse_command():
    global parse
    google_sheet_db = cur.execute('SELECT * FROM users').fetchall()
    parse = google_sheet_db


async def sql_delete_command(user_id, message: types.Message, state):
    global del_check
    revision = cur.execute(
        "SELECT * FROM users WHERE id == ?", [user_id]).fetchone()
    if revision is not None:
        cur.execute('DELETE FROM users WHERE id == ?', [user_id])
        base.commit()
        del_check = True
    else:
        await message.reply("Заявки с таким ID не существует!", reply_markup=kb.admin_main_markup)
        await state.finish()
        del_check = False
