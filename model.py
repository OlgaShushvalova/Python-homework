from asyncio import constants


path = 'phonebook.txt'
contacts = []

def read_file():
    global contacts
    with open(path) as f:
        contacts = [i.strip().split(';') for i in f.readlines()]
    return contacts

def get_contacts():
    global contacts
    return contacts

def add_contact():
    global contacts
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите описание: ')
    contacts.append(';'.join([surname, name, phone, comment]))

def save_file():
    global contacts
    with open(path, 'w', encoding='utf_8') as f:
        pass