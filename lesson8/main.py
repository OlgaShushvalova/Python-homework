import student_info as si


def option():
    question = int(input('Введите необходимую команду: \
    \n1: Поиск ученика по фамилии \
    \n2: Добавить ученика  \
    \n3: Добавить оценку за предмет ученику \
    \n4: Показать список учеников \
    \n5: Выход \n'))

    if question == 1:
        surn = str(input("Введите фамилию ученика: "))
        if surn in si.stud_card['Фамилия']:
            index = si.stud_card['Фамилия'].index(surn)
        print(
            f"{si.stud_card['Фамилия'][index]}, {si.stud_card['Имя'][index]},{si.stud_card['Класс'][index]}")
        print('\n Выполнить другую команду? Да или Нет: ')
        num = input()
        if num == 'Да' or 'ДА' or 'да':
            option()
        exit()

    elif question == 2:
        def add_student():
            surname = input('Введите фамилию: ')
            name = input('Введите имя: ')
            clas = input('Введите класс: ')
            si.stud_card['Фамилия'].append(surname)
            si.stud_card['Имя'].append(name)
            si.stud_card['Класс'].append(clas)
        add_student()
        print('\n Выполнить другую команду? Да или Нет: ')
        num = input()
        if num == 'Да' or 'ДА' or 'да':
            option()
        exit()

    elif question == 3:
        def add_rating():
            object = input('Введите предмет: ')
            rating = input('Введите оценку: ')
            si.stud_card['Предмет'].append(object)
            si.stud_card['Оценка'].append(rating)
        add_rating()
        print('\n Выполнить другую команду? Да или Нет: ')
        num = input()
        if num == 'Да' or 'ДА' or 'да':
            option()
        exit()

    elif question == 4:
        print(si.list)
        print('\n Выполнить другую команду? Да или Нет: ')
        num = input()
        if num == 'Да' or 'ДА' or 'да':
            option()
        exit()

    else:
        exit()


option()
