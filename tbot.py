import telebot
import requests
import json
bot = telebot.TeleBot('6173533762:AAF66GJccEOTx0WggSDgWZPlZvH-ajnQKpY')
API = '5a54136329c2335fc873e084eff143c4'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id , 'Привет, введи название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        bot.reply_to(message , f'{city} температура: {data["main"]["temp"]} градусов Цельсия \n {city} процент влажности: {data["main"]["humidity"]}% \n {city} скорость ветра: {data["wind"]["speed"]}м/с')
    else:
        bot.reply_to(message , 'Такого города не существует')
bot.infinity_polling()
