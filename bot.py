import telebot
from bot_config import token
from keyboard import get_main_keyboard, get_notes_numbers_keyboard, get_notes_keyboard
from database import *


bot = telebot.TeleBot(token)

users = {}

@bot.callback_query_handler(func=lambda button: True)
def reaction_to_button(button):
    user_id = button.from_user.id
    if button.data == "show_notes":
        bot.send_message(user_id, text=get_formatted_notes(user_id))
    elif button.data == "add_note":
        users.update({user_id: {'title': None, 'description': None}})
        msg = bot.send_message(user_id, text="Введите название")
        bot.register_next_step_handler(msg, note_title_answer)
    elif button.data == 'delete_note':
        bot.send_message(user_id, text="Укажите номер заметки")
        msg = bot.send_message(user_id, text=get_formatted_notes(user_id), reply_markup=get_notes_numbers_keyboard(user_id))
        bot.register_next_step_handler(msg, delete_note_number_answer)
    elif button.data == 'edit_note':
        msg = bot.send_message(user_id, text='укажити заметку', reply_markup=get_notes_keyboard(user_id))
        bot.register_next_step_handler(msg, edit_note_answer)


def edit_note_answer(message):
    user_id = message.from_user.id
    edit_id = get_id_from_title(message.text)
    users.update({user_id : {'edit_id': edit_id, 'title': None, 'description': None}})
    msg = bot.send_message(user_id, text="Введите название")
    bot.register_next_step_handler(msg, edit_title_answer)


def edit_title_answer(message):
    user_id = message.from_user.id
    users[user_id]['title'] = message.text
    msg = bot.send_message(user_id, text="Введите описание")
    bot.register_next_step_handler(msg, edit_description_answer)


def edit_description_answer(message):
    users[message.from_user.id]['description'] = message.text
    msg_text = edit_note(users[message.from_user.id]['edit_id'],
              users[message.from_user.id]['title'],
              users[message.from_user.id]['description'])
    bot.send_message(message.from_user.id, msg_text)
    

def delete_note_number_answer(message):
    user_id = message.from_user.id
    if message.text.isdigit():
        note_number = int(message.text)
        msg_text = delete_note(note_number, user_id)
        bot.send_message(user_id, msg_text)
    else:
        msg = bot.send_message(user_id, text="Нужно нажать на кнопку с номером!")
        bot.register_next_step_handler(msg, delete_note_number_answer)
      

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
