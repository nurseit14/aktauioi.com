import telebot
from telebot import types
bot = telebot.TeleBot('6421947362:AAFgeMETh6yqIbVTG7gYXKLd-QskdR-8TvE')
@bot.message_handler(commands=['start'])
def region(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} ! This bot will help you decide on a university according to your result on various tests and exams')
    region_markup = types.ReplyKeyboardMarkup(row_width = 3)
    eur = types.KeyboardButton('Europe')
    asia = types.KeyboardButton('Asia')
    africa = types.KeyboardButton('Africa')
    americal = types.KeyboardButton('Latin America')
    american = types.KeyboardButton('North America')
    oceania = types.KeyboardButton('Oceania')
    region_markup.add(eur, asia, africa, americal, american, oceania)
    bot.send_message(message.chat.id, 'Choose region where you want to study:', reply_markup=region_markup)
    bot.register_next_step_handler(message , on_click)
def on_click(message):
    reg = message.text
    bot.reply_to(message , f'{reg}, okay')
    bot.register_next_step_handler(message , results)
def results(message):
    results_markup = types.InlineKeyboardMarkup()
    ielts = types.InlineKeyboardButton('IELTS', callback_results='ielts')
    sat = types.InlineKeyboardButton('SAT', callback_results='sat')
    toefl = types.InlineKeyboardButton('TOEFL', callback_results='toefl')
    ent = types.InlineKeyboardButton('ENT', callback_results='ent')
    back = types.InlineKeyboardButton('Thats all' , callback_results='all')
    results_markup.add(ielts , sat , toefl , ent, back)
    bot.send_message(message.chat.id, f'{message.from_user.first_name} , now lets take a look at your exam results.' , reply_markup=results_markup)
@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.results == 'ielts':
        bot.send_message(callback.message.chat.id , 'Write your IELTS result here')
        ieltsres = callback.message.text
        bot.send_message(callback.message.chat.id , f'{ieltsres} not bad')
    if callback.results == 'sat':
        bot.send_message(callback.message.chat.id , 'Write your SAT result here')
        satres = callback.message.text
        bot.send_message(callback.message.chat.id , f'Oh, {satres} good')
    if callback.results == 'toefl':
        bot.send_message(callback.message.chat.id, 'Write your TOEFL result here')
        toeflres = callback.message.text
        bot.send_message(callback.message.chat.id , f'{toeflres} its ok')
    if callback.results == 'ent':
        bot.send_message(callback.message.chat.id, 'Write your ENT result here')
        entres = callback.message.text
        bot.send_message(callback.message.chat.id, f'{entres} not bad')
bot.polling(none_stop=True)
