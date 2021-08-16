import telebot
from bot_config import token
from keyboard import get_main_keyboard

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def greetings(message):
    user_id = message.from_user.id
    if message.text.lower() == 'привет':
        bot.send_message(user_id, "Привет!")
    else:
        bot.send_message(user_id, "Не знаю, что ответить")
    bot.send_message(user_id, text="Выбери действие", reply_markup=get_main_keyboard())


bot.polling(none_stop=True, interval=0)