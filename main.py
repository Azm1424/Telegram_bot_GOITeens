from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.dispatcher.filters import Text
from texts import *


TOKEN_API = '6619309941:AAGaQ8PCLP6afGJtlBXAA7ydOWcQv5BKgDA'


bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


allowed_users = [6620805013, 1215618465]
allowed_commands = ['Допомога', '/start', 'Перегляд доступних тем', 'Перегляд відео за темами']

async def start_message(_):
    print('Бот стартував')


@dp.message_handler(Text(equals='Перегляд відео за темами'))
async def videos_command(mes: types.Message):
    if mes.from_user.id in allowed_users:
        await mes.answer(text='Оберіть тему:', reply_markup=ikb3)
        await mes.delete()
    else:
        await mes.answer(text='Немає доступу')


@dp.message_handler(Text(equals='Допомога'))
async def help_command(mes: types.Message):
    if mes.from_user.id in allowed_users:
        await mes.answer(text=HELP_TXT, disable_web_page_preview=True)
        await mes.delete()
    else:
        await mes.answer(text='Немає доступу')


@dp.message_handler(commands=['start'])
async def start_command(mes: types.Message):
    await mes.answer(text=START_TXT, reply_markup=keyboard)


@dp.message_handler(Text(equals='Перегляд доступних тем'))
async def themes_command(mes: types.Message):
    if mes.from_user.id in allowed_users:
        await mes.answer(text='Оберіть тему:', reply_markup=ikb)
        await mes.delete()
    else:
        await mes.answer(text='Немає доступу')


@dp.callback_query_handler(Text(equals='videos_theme_1'))
async def open_video(cb: types.CallbackQuery):
    if cb.data == 'videos_theme_1':
        await bot.send_message(chat_id=cb.from_user.id, text='Оберіть частину', reply_markup=ikb4)


@dp.callback_query_handler(Text(equals='videos_theme_2'))
async def open_video(cb: types.CallbackQuery):
    if cb.data == 'videos_theme_2':
        await bot.send_message(chat_id=cb.from_user.id, text='Оберіть частину', reply_markup=ikb5)


@dp.callback_query_handler(Text(equals='videos_theme_3'))
async def open_video(cb: types.CallbackQuery):
    if cb.data == 'videos_theme_3':
        await bot.send_message(chat_id=cb.from_user.id, text='Оберіть частину', reply_markup=ikb6)


@dp.callback_query_handler()
async def open_theme(cb: types.CallbackQuery):
    if cb.data == 'theme_1':
        a = ''
        with open('theme_1.txt', 'r', encoding='utf-8') as t1:
            lst_txt = t1.readlines()
        for i in range(11):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML', reply_markup=ikb_t_1_2)
        await cb.answer()
    elif cb.data == 'part_1_2':
        with open('theme_1.txt', 'r', encoding='utf-8') as t1:
            lst_txt = t1.readlines()
        a = ''
        for i in range(12, 25):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML')
        await cb.answer()
        for k, v in THEME_1_1_PHOTO.items():
            await bot.send_photo(chat_id=cb.from_user.id, photo=k, caption=v)
            await cb.answer()
        await bot.send_message(chat_id=cb.from_user.id, text='Продовжити', reply_markup=ikb_t_1_3)
    elif cb.data == 'part_1_3':
        with open('theme_1.txt', 'r', encoding='utf-8') as t1:
            lst_txt = t1.readlines()
        a = ''
        for i in range(26, 48):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML')
        await cb.answer()
    elif cb.data == 'theme_2':
        with open('theme_2.txt', 'r', encoding='utf-8') as t2:
            lst_txt = t2.readlines()
            a = ''
            for i in range(17):
                a += lst_txt[i]
            await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML', reply_markup=ikb_t_2_2)
            await cb.answer()
    elif cb.data == 'part_2_2':
        with open('theme_2.txt', 'r', encoding='utf-8') as t2:
            lst_txt = t2.readlines()
        a = ''
        for i in range(18, 34):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, reply_markup=ikb_t_2_3)
        await cb.answer()
    elif cb.data == 'part_2_3':
        with open('theme_2.txt', 'r', encoding='utf-8') as t2:
            lst_txt = t2.readlines()
        a = ''
        for i in range(35, 48):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML')
        await cb.answer()
    elif cb.data == 'theme_3':
        with open('theme_3.txt', 'r', encoding='utf-8') as t3:
            lst_txt = t3.readlines()
            a = ''
            for i in range(14):
                a += lst_txt[i]
            await bot.send_message(chat_id=cb.from_user.id, text=a, parse_mode='HTML', reply_markup=ikb_t_3_2)
            await cb.answer()
    elif cb.data == 'part_3_2':
        with open('theme_3.txt', 'r', encoding='utf-8') as t3:
            lst_txt = t3.readlines()
        a = ''
        for i in range(15, 33):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a, reply_markup=ikb_t_3_3, parse_mode='HTML')
        await cb.answer()
    elif cb.data == 'part_3_3':
        with open('theme_3.txt', 'r', encoding='utf-8') as t3:
            lst_txt = t3.readlines()
        a = ''
        for i in range(34, 82):
            a += lst_txt[i]
        await bot.send_message(chat_id=cb.from_user.id, text=a)
        await cb.answer()
        for k, v in THEME_3_3_PHOTO.items():
            await bot.send_photo(chat_id=cb.from_user.id, photo=k, caption=v)
            await cb.answer()


@dp.message_handler()
async def del_garbage(mes: types.Message):
    if mes.text not in allowed_commands:
        await mes.delete()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start_message, skip_updates=True,
                           allowed_updates=['message', 'inline_query', 'callback_query'])
