import telebot
from telebot import types

TOKEN = '966690951:AAEQeVK0aHPsHuTek8RQAieynjtVgFjuMY4'
bot = telebot.TeleBot(TOKEN)
markup = types.ReplyKeyboardMarkup(row_width=2)
getAppLink = types.KeyboardButton('Получить ссылку')
markup.add(getAppLink)
bot.send_message("Привет! Я телеграм-бот приложения Smart Svit. Сейчас я могу выполнить только одно действие - поделиться с тобой ссылкой на скачивание приложения. Но скоро я научусь и другим вещам. До встречи :)", reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_handler(message: types.Message):
    bot.reply_to(message, ":)")


@bot.message_handler(content_types=['text'])
def message_handler(message: types.Message):
    bot.reply_to(message, 'Извини, я тебя не понимаю :)')


bot.polling()
