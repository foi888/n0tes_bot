import telebot
from telebot import types


def get_main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    show_notes_btn = types.InlineKeyboardButton("Показать заметки", callback_data="show_notes")
    add_note_btn = types.InlineKeyboardButton("Добавить заметку", callback_data="add_note")
    edit_note_btn = types.InlineKeyboardButton("Редактировать заметку", callback_data="edit_note")
    delete_note_btn = types.InlineKeyboardButton("Удалить заметку", callback_data="delete_note")
    keyboard.add(show_notes_btn, add_note_btn, edit_note_btn, delete_note_btn)
    return keyboard
