import telebot
from telebot import types
from database import get_notes

def get_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    show_notes_btn = types.InlineKeyboardButton("Показать заметки", callback_data="show_notes")
    add_note_btn = types.InlineKeyboardButton("Добавить заметку", callback_data="add_note")
    edit_note_btn = types.InlineKeyboardButton("Редактировать заметку", callback_data="edit_note")
    delete_note_btn = types.InlineKeyboardButton("Удалить заметку", callback_data="delete_note")
    keyboard.add(show_notes_btn, add_note_btn, edit_note_btn, delete_note_btn)
    return keyboard


def get_notes_numbers_keyboard(user_id):
    keyboard = types.ReplyKeyboardMarkup()
    notes = get_notes(user_id)
    if notes:
        for i in range (1, len(notes)+1):
            keyboard.add(types.KeyboardButton(str(i)))
    else:
        button = types.KeyboardButton("продолжить")
        keyboard.add(button)
    return keyboard



