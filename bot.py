import telebot
from bot_config import token
from keyboard import get_main_keyboard
from database import *


bot = telebot.TeleBot(token)

users = {}

@bot.callback_query_handler(func=lambda button: True)
def reaction_to_button(button):
    user_id = button.from_user.id
    if button.data == "show_notes":
        bot.send_message(user_id, text=get_formatted_notes(user_id))
    if button.data == "add_note":
        users.update({user_id: {'title': None, 'description': None}})
        msg = bot.send_message(user_id, text="введите название")
        bot.register_next_step_handler(msg, note_title_answer)
    if button.data == 'delete_note':
        pass

        

def note_title_answer(message):
    users[message.from_user.id]["title"] = message.text
    msg = bot.send_message(message.from_user.id, text="Введите описание")
    bot.register_next_step_handler(msg, note_description_answer)


def note_description_answer(message):
    users[message.from_user.id]["description"] = message.text
    msg_text = send_note(message.from_user.id, 
                         users[message.from_user.id]["title"],
                         users[message.from_user.id]["description"])
    bot.send_message(message.from_user.id, text=msg_text)


@bot.message_handler(content_types=['text'])
def reaction_to_text(message):
    user_id = message.from_user.id
    if message.text.lower() == 'привет':
        bot.send_message(user_id, "Привет!")
    else:
        bot.send_message(user_id, "Не знаю, что ответить")
    bot.send_message(user_id, text="Выбери действие", reply_markup=get_main_keyboard())


bot.polling(none_stop=True, interval=0)