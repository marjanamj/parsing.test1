import requests
import telebot
from bs4 import BeautifulSoup as b
import random

URL = 'https://kaktus.media/?lable=8&date=2024-02-02&order=time'
API_KEY = '6450621951:AAFD9rtrsMsVO-iGl05l4quDNUwAH1MMugo'
def parser(url):
    r = requests.get(url)
    soup =b(r.text,'html.parser')
    news = soup.find_all('div', class_='Tag--article')
    return [c.text for c in news]

list_of_news = parser(URL)
random.shuffle(list_of_news)
 
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет чтобы посмотреть новости введите любую цифру:')

@bot.message_handler(content_types=['text'])
def news(message):
    if message.text.lower() in '1, 2, 3, 4, 5, 6, 7, 8, 9':
        bot.send_message(message.chat.id, list_of_news[0])
        del list_of_news [0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру:')




bot.polling()
    
    
