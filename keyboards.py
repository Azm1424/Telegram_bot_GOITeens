from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='Допомога')
b2 = KeyboardButton(text='Перегляд доступних тем')
b3 = KeyboardButton(text='Перегляд відео за темами')
keyboard.add(b1).insert(b2).add(b3)


ikb = InlineKeyboardMarkup(row_width=2)
ikb_1, ikb_2, ikb_3 = (InlineKeyboardButton(text='Вступ. Що таке Python?', callback_data='theme_1'),
                       InlineKeyboardButton(text='Основи мови — змінні та вирази', callback_data='theme_2'),
                       InlineKeyboardButton(text='Умовні оператори', callback_data='theme_3'))
ikb.add(ikb_1).add(ikb_2).add(ikb_3)

ikb_t_1_2 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_1_2')
ikb_t_1_2.add(ikb_dali)

ikb_t_1_3 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_1_3')
ikb_t_1_3.add(ikb_dali)

ikb_t_2_2 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_2_2')
ikb_t_2_2.add(ikb_dali)

ikb_t_2_3 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_2_3')
ikb_t_2_3.add(ikb_dali)

ikb_t_3_2 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_3_2')
ikb_t_3_2.add(ikb_dali)

ikb_t_3_3 = InlineKeyboardMarkup(row_width=2)
ikb_dali = InlineKeyboardButton(text='Далі', callback_data='part_3_3')
ikb_t_3_3.add(ikb_dali)

ikb3 = InlineKeyboardMarkup(row_width=2)
ikb_3_1, ikb_3_2, ikb_3_3 = (InlineKeyboardButton(text='Вступ. Що таке Python?', callback_data='videos_theme_1'),
                       InlineKeyboardButton(text='Основи мови — змінні та вирази', callback_data='videos_theme_2'),
                       InlineKeyboardButton(text='Умовні оператори', callback_data='videos_theme_3'))
ikb3.add(ikb_3_1).add(ikb_3_2).add(ikb_3_3)

ikb4 = InlineKeyboardMarkup(row_width=2)
ikb_4_1, ikb_4_2 = (InlineKeyboardButton(text='Частина 1', url='https://youtu.be/ewcyVtpc2F0'),
                    InlineKeyboardButton(text='Частина 2', url='https://youtu.be/MxuVL8vI68M'))
ikb4.add(ikb_4_1).insert(ikb_4_2)

ikb5 = InlineKeyboardMarkup(row_width=2)
ikb_5_1, ikb_5_2 = (InlineKeyboardButton(text='Частина 1', url='https://youtu.be/CDgMQLtlxjk'),
                    InlineKeyboardButton(text='Частина 2', url='https://youtu.be/kOkBzKc1KXI'))
ikb5.add(ikb_5_1).insert(ikb_5_2)

ikb6 = InlineKeyboardMarkup(row_width=2)
ikb_6_1, ikb_6_2 = (InlineKeyboardButton(text='Частина 1', url='https://youtu.be/bq8NvMXhr6k'),
                    InlineKeyboardButton(text='Частина 2', url='https://youtu.be/6qREKl5GPJc'))
ikb6.add(ikb_6_1).insert(ikb_6_2)