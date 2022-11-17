import view, model

def start():
    while True:
        command = view.show_menu()
        match command:
            case '1':
                view.show_contacts(model.get_contacts())
            case '2':
                model.add_contact()
            case '0':
                break
