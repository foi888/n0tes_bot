import requests
import json
from bot_config import headers


def get_notes(user_id):
    url = "https://notes-70b5.restdb.io/rest/notes?filter=" + str(user_id)
    response = requests.request("GET", url, headers=headers)
    notes = json.loads(response.text)
    return notes


def get_formatted_notes(user_id):
    notes = get_notes(user_id)
    if notes:
        count = 1
        formatted_text = ""
        for note in notes:
            formatted_text += f"{count}. Название: {note['Title']}\nОписание: {note['Description']} \n\n"
            count+=1
        return formatted_text
    else:
        return "У вас нет заметок"


def send_note(user_id, title, description):
    url = "https://notes-70b5.restdb.io/rest/notes"
    payload = json.dumps({'Title': title, 'UserId': user_id, 'Description': description})
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.ok:
        return "Заметка успешно добавлена"
    else:
        return "Произошла ошибка. Попробуйте позже"


def delete_note(note_number, user_id):
    notes = get_notes(user_id)
    if note_number in range(1, len(notes)+1):
        delete_id = notes[note_number-1]['_id']
        url = "https://notes-70b5.restdb.io/rest/notes/" + delete_id
        response = requests.request("DELETE", url, headers=headers)
        if response.ok:
            return "Успешно удалено"
        else:
            return "Произошла ошибка. Попробуйте позже"
    else:
        return("Попробуйте снова, указав верный номер")



def edit_note(note_id, title, description):
    url = "https://notes-70b5.restdb.io/rest/notes/" + note_id
    payload = json.dumps({'Title': title, 'Description': description})
    response = requests.request("PUT", url, data=payload, headers=headers)
    if response.ok:
        return 'Успешно отредактировано'
    else:
        return 'Произошла ошибка. Попробуйте позже'





def get_id_from_title(title):
    url = "https://notes-70b5.restdb.io/rest/notes?filter=" + str(title)
    response = requests.request("GET", url, headers=headers)
    note = json.loads(response.text)[0]
    return note['_id']
