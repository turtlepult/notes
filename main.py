import json
import datetime
import argparse

def add_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": str(datetime.datetime.now())
    }
    notes.append(note)
    save_notes()

def read_notes():
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print()

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            note['title'] = title
            note['message'] = message
            note['timestamp'] = str(datetime.datetime.now())
            save_notes()
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def load_notes():
    try:
        with open("notes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_notes():
    for note in notes:
        print(note['id'], note['title'])

parser = argparse.ArgumentParser(
    description="Консольное приложение для заметок")
parser.add_argument("command", choices=[
                    "add", "read", "edit", "delete", "list"],
                    help="Команда для выполнения")
parser.add_argument("--title", help="Заголовок заметки")
parser.add_argument("--msg", help="Текст заметки")

args = parser.parse_args()

notes = load_notes()

if args.command == "add":
    add_note()
elif args.command == "read":
    read_notes()
elif args.command == "edit":
    edit_note()
elif args.command == "delete":
    delete_note()
elif args.command == "list":
    list_notes()