import pandas as pd


stud_card = {
    'Фамилия': ['Иванов', 'Петров', 'Сидоров'],
    'Имя': ['Николай', 'Василий', 'Сергей'],
    'Класс': ['7а', '7б', '7в'],
    'Предмет': ['Математика', 'История', 'Физика'],
    'Оценка': ['4', '3', '3']
}

list = pd.DataFrame(data=stud_card)

with open('students.csv', 'w', encoding='UTF-8') as cl:
    cl.write('f {list}')
    cl.write('\n')
