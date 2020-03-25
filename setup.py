import telebot
from telebot.types import Message

TOKEN = '966690951:AAEQeVK0aHPsHuTek8RQAieynjtVgFjuMY4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message: Message):
    bot.reply_to(message, "Привет! Я телеграм-бот приложения Smart Svit. Сейчас я могу выполнить только одно действие - поделиться с тобой ссылкой на скачивание приложения. Но скоро я научусь и другим вещам. До встречи :)")


@bot.message_handler(commands=['help'])
def help_handler(message: Message):
    bot.reply_to(message, "Help clicked")


@bot.message_handler(content_types=['text'])
def message_handler(message: Message):
    bot.reply_to(message, 'hello there')


bot.polling()
