import telebot
from bot_config import token
from keyboard import get_main_keyboard
from database import *

bot = telebot.TeleBot(token)


@bot.callback_query_handler(func=lambda call: True)
def reaction_to_button(call):
    user_id = call.from_user.id
    if call.data == "show_notes":
        bot.send_message(user_id, text=get_formatted_notes(user_id))
        

@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    user_id = message.from_user.id
    print(user_id)
    if message.text.lower() == 'привет':
        bot.send_message(user_id, "Привет!")
    else:
        bot.send_message(user_id, "Не знаю, что ответить")
    bot.send_message(user_id, text="Выбери действие", reply_markup=get_main_keyboard())


bot.polling(none_stop=True, interval=0)