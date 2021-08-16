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
    if notes == []:
        return "У вас нет заметок. Создайте"
    formatted_text = ""
    for note in notes:
        formatted_text += f"Название: {note['Title']}\nОписание: {note['Description']} \n\n"
    return formatted_text
    
