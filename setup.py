import telebot
from telebot import types

TOKEN = '966690951:AAEQeVK0aHPsHuTek8RQAieynjtVgFjuMY4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn_app = types.InlineKeyboardButton(
        text='Получить ссылку', url='https://play.google.com/store/apps/details?id=com.smartsvitapp')
    markup.add(btn_app)
    bot.reply_to(message, "Привет! Я телеграм-бот приложения Smart Svit. Сейчас я могу выполнить только одно действие - поделиться с тобой ссылкой на скачивание приложения. Но скоро я научусь и другим вещам. До встречи :)")
    bot.send_message(
        message.chat.id, "Нажми на кнопку и получи приложение для Android", reply_markup=markup)


bot.polling()
