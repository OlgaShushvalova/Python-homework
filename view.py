def show_menu():
    question = 'Введите необходимую команду:\
        \n1 - Показать все контакты\
        \n2 - Добавить контакт\
        \n0 - Выход\
        \n'
    command = input(question)
    return command

def show_contacts(contacts: list):
    [print(contact) for contact in contacts]